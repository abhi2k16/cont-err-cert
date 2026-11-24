"""E1 (archive/SHORT_PAPER_SCOPE.md): exactness of the S1 certificate on finite element queries (X = K, constant-K benchmarks).

For every test query, basis size and correction (R0; R0s with the gap rule tau_g = config.TAU_GAP; R0s with the multiplier rule,
which over-snaps) the corrected u^ is certified with S1 and X = K (alpha = 1), and compared with the full-order solution:
  condition (C):  0 <= g^ <= 2 g  componentwise (tolerance 1e-12 * char_gap; g from the full-order solution)
  Cor. 3.5:       (C)  =>  Delta* = ||e||_K  (effectivity 1)
  Thm 3.7:        otherwise  1 <= eff <= (2/sqrt3) (1 + sqrt(m(M)/||e||)),  M = {i : lam_i > 0, g^_i > tol}
Criterion (fixed in archive/SHORT_PAPER_SCOPE.md before running): where (C) holds |eff - 1| <= 1e-6; elsewhere the bounds above hold
(within 1e-9 relative). The fraction of queries satisfying (C) is reported per correction.

Output: results/e1_exactness/<problem>_seed<seed>.npz and a JSON summary.
Usage:  python experiments/e1.py --problem membrane --seed 0
"""

import json
import logging

import numpy as np

from certcorrect import cli
from certcorrect.active_set import by_gap, by_multiplier
from certcorrect.certificate import certify
from certcorrect.config import RESULTS, SEEDS, SETTINGS, TAU_GAP, TAU_LAMBDA, make_problem, result_path
from certcorrect.corrections import RightInverse, repair_r0_snap
from certcorrect.fom import energy_norm
from certcorrect.multipliers import MinResidualS1
from certcorrect.pipeline import EnergyInnerProduct, build_bases, rom_for_size, solve_many, training_snapshots
from certcorrect.results_io import save_result

LOG = logging.getLogger("e1_exactness")
EXPERIMENT = "e1_exactness"
CORRECTIONS = ("R0", "R0s_gap", "R0s_mult")
SQRT3 = np.sqrt(3.0)
EXACT_TOL = 1e-6          # |eff - 1| where condition (C) holds
BOUND_TOL = 1e-9          # relative slack of the bounds
GAP_TOL = 1e-12           # times char_gap


def active_set(kind: str, red, problem, c) -> np.ndarray:
    if kind == "R0":
        return np.zeros(0, dtype=int)
    if kind == "R0s_gap":
        return by_gap(problem.B @ red.u - c, TAU_GAP, problem.char_gap)
    return by_multiplier(red.lam, TAU_LAMBDA)


def run(problem, settings: dict, seed: int) -> dict:
    if problem.k_varies:
        raise ValueError("E1 uses X = K and is defined for a constant K (membrane, block)")
    snap = training_snapshots(problem, np.random.default_rng(SEEDS["train"] + seed), settings["n_train"])
    V, W = build_bases(snap, max(settings["r_primal"]), settings["r_dual"], settings["dual_kind"])
    mus = problem.sample_test(np.random.default_rng(SEEDS["test"] + seed), settings["n_test"])
    refs, ok = solve_many(problem, mus, "test")
    mus = mus[ok]
    inner = EnergyInnerProduct(problem)                    # constant K: X = K(mu_bar) = K, alpha = 1
    Bp, s1, B = RightInverse.from_constraints(problem.B), MinResidualS1(problem.B, inner.solve), problem.B
    tol_gap = GAP_TOL * problem.char_gap
    fields = ("eff", "cond", "bound", "m_missed", "error")
    out = {f"{k}_{c}": [] for k in fields for c in CORRECTIONS}
    out["r"] = {c: [] for c in CORRECTIONS}
    for r in [r for r in settings["r_primal"] if r <= V.shape[1]]:
        rom = rom_for_size(problem, V, W, r)
        for mu, ref in zip(mus, refs):
            K, f, c = problem.stiffness(mu), problem.load(mu), problem.offset(mu)
            red = rom.solve(mu)
            if not red.converged:
                continue
            for kind in CORRECTIONS:
                u_hat = repair_r0_snap(red.u, B, c, Bp, active_set(kind, red, problem, c))
                g_hat = np.maximum(B @ u_hat - c, 0.0)
                ell, _ = s1.solve(f - K @ u_hat, g_hat, 1.0)
                delta = certify(K, f, B, c, u_hat, ell, inner.solve, 1.0).delta
                e = energy_norm(K, ref.u - u_hat)
                missed = (ref.lam > 0) & (g_hat > tol_gap)
                lam_m = np.where(missed, ref.lam, 0.0)
                v = B.T @ lam_m
                m_missed = float(np.sqrt(max(v @ inner.solve(v), 0.0)))
                cond = bool((g_hat <= 2 * ref.gap + tol_gap).all())
                out[f"eff_{kind}"].append(delta / e)
                out[f"cond_{kind}"].append(cond)
                out[f"bound_{kind}"].append((2 / SQRT3) * (1 + np.sqrt(m_missed / e)))
                out[f"m_missed_{kind}"].append(m_missed)
                out[f"error_{kind}"].append(e / energy_norm(K, ref.u))
                out["r"][kind].append(r)
    return {k: (np.array(v) if not isinstance(v, dict) else {c: np.array(x) for c, x in v.items()})
            for k, v in out.items()}


def summarise(out: dict) -> dict:
    summary = {}
    for kind in CORRECTIONS:
        eff, cond, bound = out[f"eff_{kind}"], out[f"cond_{kind}"], out[f"bound_{kind}"]
        exact = np.abs(eff[cond] - 1.0) if cond.any() else np.array([0.0])
        within = (eff[~cond] >= 1 - BOUND_TOL) & (eff[~cond] <= bound[~cond] * (1 + BOUND_TOL))
        summary[kind] = {"queries": int(len(eff)), "share_condition_holds": float(cond.mean()),
                         "n_condition": int(cond.sum()), "max_abs_eff_minus_1_where_condition": float(exact.max()),
                         "exactness_violations": int((exact > EXACT_TOL).sum()) if cond.any() else 0,
                         "n_other": int((~cond).sum()),
                         "bound_violations": int((~within).sum()) if (~cond).any() else 0,
                         "eff_median_other": float(np.median(eff[~cond])) if (~cond).any() else None,
                         "eff_max_other": float(eff[~cond].max()) if (~cond).any() else None}
    return summary


def main(args) -> int:
    problem = make_problem(args.problem)
    path = result_path(EXPERIMENT, args.problem, args.seed)
    LOG.info("%s (constant K, X = K), tau_g = %g -> %s", problem.name, TAU_GAP, path)
    if args.dry_run:
        return cli.EXIT_OK
    out = run(problem, SETTINGS[args.problem], args.seed)
    summary = summarise(out)
    for kind, s in summary.items():
        LOG.info("%-8s %5d queries | condition (C) holds for %5.1f %% | where it holds: max |eff-1| = %.1e, violations %d | "
                 "elsewhere (%d): eff median %s, max %s, bound violations %d", kind, s["queries"],
                 100 * s["share_condition_holds"], s["max_abs_eff_minus_1_where_condition"], s["exactness_violations"],
                 s["n_other"], "n/a" if s["eff_median_other"] is None else f"{s['eff_median_other']:.3f}",
                 "n/a" if s["eff_max_other"] is None else f"{s['eff_max_other']:.3f}", s["bound_violations"])
    flat = {k: v for k, v in out.items() if not isinstance(v, dict)}
    save_result(path, flat, {"experiment": EXPERIMENT, "problem": args.problem, "seed": args.seed,
                             "tau_gap": TAU_GAP, "summary": summary})
    json_path = RESULTS / EXPERIMENT / f"{args.problem}_seed{args.seed}.json"
    json_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    bad = sum(s["exactness_violations"] + s["bound_violations"] for s in summary.values())
    return cli.EXIT_OK if bad == 0 else cli.EXIT_FAILURE


if __name__ == "__main__":
    cli.run(main, cli.base_parser(__doc__.splitlines()[0]))
