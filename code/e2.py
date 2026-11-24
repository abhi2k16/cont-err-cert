"""E2 (archive/SHORT_PAPER_SCOPE.md): the support floor of the restricted S1 multiplier on the controlled lift-off sequence.

For a full-order solution (u, lam) let phi = K^-1 B^T lam / ||.||_K (>= 0 for the M-matrix benchmarks). The predictions
u~_eps = u + eps phi (rows opened at fixed force), corrected by R0-snap on the exact strictly active set A_+ (so u^ is consistent and
the error is exactly of order eps), are certified with X = K (alpha = 1) using
  full     S1 on all rows,
  omit_i*  S1 on all rows except the strictly active row i* of largest force,
  omit_A   S1 on A_+ without i* (rows outside A_+ also dropped).
sigma_S = min_v ||B^T lam_{S^c} - B_S^T v||_{K^-1} is computed offline (certcorrect.theory.support_floor).
For the membrane K is an M-matrix, so phi >= 0 and the sequence is the "rows opened at fixed force" picture; for the block it is not,
phi may have negative entries, and R0-snap on A_+ (with R0 on the other rows) still gives a feasible, consistent u^ with error of order eps:
the statements tested need only g^ = 0 on A_+.

Criterion (fixed in archive/SHORT_PAPER_SCOPE.md before running), at the smallest amplitude: certificate of the restricted multiplier
>= 0.95 sigma_S / sqrt(alpha_X) and >= 100 x the full-S1 certificate; the full-S1 certificate has rate 1 in the error.

Output: results/e2_support_floor/<problem>_seed<seed>.npz.   Usage:  python experiments/e2.py --problem membrane --seed 0
"""

import json
import logging

import numpy as np
from scipy.sparse.linalg import factorized

from certcorrect import cli
from certcorrect.analysis import loglog_slope
from certcorrect.certificate import certify
from certcorrect.config import RESULTS, SEEDS, make_problem, result_path
from certcorrect.corrections import RightInverse, repair_r0_snap
from certcorrect.fom import FullOrderSolver, energy_norm
from certcorrect.multipliers import MinResidualS1
from certcorrect.results_io import save_result
from certcorrect.theory import support_floor

LOG = logging.getLogger("e2_support_floor")
EXPERIMENT = "e2_support_floor"
EPSILONS = np.geomspace(1e-1, 1e-6, 11)
N_QUERIES = 10
SUPPORTS = ("full", "omit_i", "omit_A")
FLOOR_FRACTION, STALL_FACTOR = 0.95, 100.0


def run(problem, seed: int) -> dict:
    if problem.k_varies:
        raise ValueError("E2 uses X = K and is defined for a constant K")
    K = problem.stiffness(problem.lo)
    solve_k = factorized(K.tocsc())
    B, Bp, s1 = problem.B, RightInverse.from_constraints(problem.B), MinResidualS1(problem.B, solve_k)
    mus = problem.sample_test(np.random.default_rng(SEEDS["test"] + seed), N_QUERIES)
    n_q = N_QUERIES
    out = {"eps": EPSILONS, "error": np.full((n_q, len(EPSILONS)), np.nan), "sigma": {s: np.full(n_q, np.nan) for s in SUPPORTS}}
    out.update({f"delta_{s}": np.full((n_q, len(EPSILONS)), np.nan) for s in SUPPORTS})
    for i, mu in enumerate(mus):
        f, c = problem.load(mu), problem.offset(mu)
        ref = FullOrderSolver(problem).solve(mu, K=K)
        plus = ref.strictly_active
        if not ref.converged or plus.size < 2:
            continue
        phi = solve_k(B.T @ ref.lam)
        phi *= energy_norm(K, ref.u) / energy_norm(K, phi)
        istar = plus[np.argmax(ref.lam[plus])]
        supports = {"full": None, "omit_i": np.setdiff1d(np.arange(problem.n_contact), [istar]),
                    "omit_A": np.setdiff1d(plus, [istar])}
        for name, support in supports.items():
            out["sigma"][name][i] = 0.0 if support is None else support_floor(B, ref.lam, support, solve_k)
        for j, eps in enumerate(EPSILONS):
            u_hat = repair_r0_snap(ref.u + eps * phi, B, c, Bp, plus)
            g_hat = np.maximum(B @ u_hat - c, 0.0)
            out["error"][i, j] = energy_norm(K, ref.u - u_hat)
            for name, support in supports.items():
                ell, _ = s1.solve(f - K @ u_hat, g_hat, 1.0, support)
                out[f"delta_{name}"][i, j] = certify(K, f, B, c, u_hat, ell, solve_k, 1.0).delta
    return out


def summarise(out: dict) -> dict:
    last = -1
    ok = np.isfinite(out["error"][:, last])
    summary = {"n_queries": int(ok.sum()), "rate_full": loglog_slope(out["error"][ok].ravel(), out["delta_full"][ok].ravel())}
    for name in ("omit_i", "omit_A"):
        d, sigma = out[f"delta_{name}"][ok, last], out["sigma"][name][ok]
        summary[name] = {"min_ratio_to_floor": float((d / sigma).min()),
                         "min_ratio_to_full": float((d / out["delta_full"][ok, last]).min()),
                         "floor_violations": int((d < FLOOR_FRACTION * sigma).sum()),
                         "stall_violations": int((d < STALL_FACTOR * out["delta_full"][ok, last]).sum()),
                         "sigma_median": float(np.median(sigma)),
                         "delta_at_largest_eps_median": float(np.median(out[f"delta_{name}"][ok, 0]))}
    return summary


def main(args) -> int:
    problem = make_problem(args.problem)
    path = result_path(EXPERIMENT, args.problem, args.seed)
    LOG.info("%s: %d queries x %d amplitudes -> %s", problem.name, N_QUERIES, len(EPSILONS), path)
    if args.dry_run:
        return cli.EXIT_OK
    out = run(problem, args.seed)
    summary = summarise(out)
    LOG.info("full S1: certificate rate in the error %.3f over %d queries", summary["rate_full"], summary["n_queries"])
    for name in ("omit_i", "omit_A"):
        s = summary[name]
        LOG.info("%-7s: at the smallest eps, delta/sigma_S >= %.3f (floor violations %d), delta/delta_full >= %.1f (stall "
                 "violations %d); median sigma_S %.3e, median delta at eps = 0.1: %.3e", name, s["min_ratio_to_floor"],
                 s["floor_violations"], s["min_ratio_to_full"], s["stall_violations"], s["sigma_median"],
                 s["delta_at_largest_eps_median"])
    flat = {k: v for k, v in out.items() if not isinstance(v, dict)}
    flat.update({f"sigma_{s}": v for s, v in out["sigma"].items()})
    save_result(path, flat, {"experiment": EXPERIMENT, "problem": args.problem, "seed": args.seed, "summary": summary})
    (RESULTS / EXPERIMENT / f"{args.problem}_seed{args.seed}.json").write_text(json.dumps(summary, indent=2),
                                                                             encoding="utf-8")
    bad = sum(summary[n]["floor_violations"] + summary[n]["stall_violations"] for n in ("omit_i", "omit_A"))
    return cli.EXIT_OK if bad == 0 else cli.EXIT_FAILURE


if __name__ == "__main__":
    cli.run(main, cli.base_parser(__doc__.splitlines()[0]))
