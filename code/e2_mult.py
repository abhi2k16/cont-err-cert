"""E2 follow-up: are the restricted S1 multipliers of the two E2 supports equal, and zero outside A_+?

Same controlled sequence as e2.py. For the supports "all rows but i*" and "A_+ without i*" the restricted S1 multipliers are
computed; reported (relative to the largest entry of the first multiplier): its largest entry on the rows outside A_+, and the largest
difference between the two multipliers on A_+ without i*. This is a diagnostic only (no acceptance criterion).

Output: results/e2_support_floor/multiplier_check_<problem>_seed<seed>.json.   Usage:  python experiments/e2_mult.py --problem membrane --seed 0
"""

import json
import logging

import numpy as np
from scipy.sparse.linalg import factorized

from certcorrect import cli
from certcorrect.config import RESULTS, SEEDS, make_problem
from certcorrect.corrections import RightInverse, repair_r0_snap
from certcorrect.fom import FullOrderSolver, energy_norm
from certcorrect.multipliers import MinResidualS1

LOG = logging.getLogger("e2_multiplier_check")
EPSILONS = np.geomspace(1e-1, 1e-6, 11)
N_QUERIES = 10


def run(problem, seed: int) -> dict:
    if problem.k_varies:
        raise ValueError("defined for a constant K")
    K = problem.stiffness(problem.lo)
    solve_k = factorized(K.tocsc())
    B, Bp, s1 = problem.B, RightInverse.from_constraints(problem.B), MinResidualS1(problem.B, solve_k)
    outside_rel, diff_rel, eps_of_worst = [], [], []
    for mu in problem.sample_test(np.random.default_rng(SEEDS["test"] + seed), N_QUERIES):
        f, c = problem.load(mu), problem.offset(mu)
        ref = FullOrderSolver(problem).solve(mu, K=K)
        plus = ref.strictly_active
        if not ref.converged or plus.size < 2:
            continue
        phi = solve_k(B.T @ ref.lam)
        phi *= energy_norm(K, ref.u) / energy_norm(K, phi)
        istar = plus[np.argmax(ref.lam[plus])]
        all_but = np.setdiff1d(np.arange(problem.n_contact), [istar])
        a_minus = np.setdiff1d(plus, [istar])
        outside = np.setdiff1d(all_but, plus)
        for eps in EPSILONS:
            u_hat = repair_r0_snap(ref.u + eps * phi, B, c, Bp, plus)
            g_hat = np.maximum(B @ u_hat - c, 0.0)
            l1, _ = s1.solve(f - K @ u_hat, g_hat, 1.0, all_but)
            l2, _ = s1.solve(f - K @ u_hat, g_hat, 1.0, a_minus)
            scale = max(np.abs(l1).max(), 1e-300)
            outside_rel.append(float(np.abs(l1[outside]).max() / scale) if outside.size else 0.0)
            diff_rel.append(float(np.abs(l1[a_minus] - l2[a_minus]).max() / scale))
            eps_of_worst.append(float(eps))
    out, diff, eps = np.array(outside_rel), np.array(diff_rel), np.array(eps_of_worst)
    small = eps <= 1e-3
    return {"cases": int(out.size), "max_outside_Aplus_relative": float(out.max()), "max_difference_on_Aplus_relative": float(diff.max()),
            "max_outside_Aplus_relative_eps_le_1e-3": float(out[small].max()),
            "max_difference_on_Aplus_relative_eps_le_1e-3": float(diff[small].max())}


def main(args) -> int:
    problem = make_problem(args.problem)
    path = RESULTS / "e2_support_floor" / f"multiplier_check_{args.problem}_seed{args.seed}.json"
    LOG.info("%s seed %d -> %s", problem.name, args.seed, path)
    if args.dry_run:
        return cli.EXIT_OK
    summary = run(problem, args.seed)
    LOG.info("%s", summary)
    path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    return cli.EXIT_OK


if __name__ == "__main__":
    cli.run(main, cli.base_parser(__doc__.splitlines()[0]))
