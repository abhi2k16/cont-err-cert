"""Half-rate example of Proposition 4.1 (N = 2, n_c = 1, K = I, B = [1 0], c = 0, f = (-1, 0), X = K, u^ = (eps, 0)).

For each eps the certificate is evaluated with the certcorrect certificate code on a fine grid of multipliers; the minimum over l >= 0 is refined with a
bounded scalar minimiser, and the certificate of the S1 multiplier is computed with certcorrect.multipliers.MinResidualS1. Compared with the closed form
sqrt(eps (1 + eps)) of Proposition 4.1 (no tolerance is imposed; the maximum relative deviation is reported).

Output: results/e_halfrate/halfrate.npz and halfrate.json.   Usage:  python experiments/halfrate.py
"""

import json
import logging
import sys

import numpy as np
from scipy.optimize import minimize_scalar

from certcorrect.certificate import certify
from certcorrect.cli import EXIT_OK, setup_logging
from certcorrect.config import RESULTS
from certcorrect.multipliers import MinResidualS1
from certcorrect.results_io import save_result

LOG = logging.getLogger("e_halfrate")
EPSILONS = np.geomspace(1e-8, 1.0, 33)


def identity_solve(v):
    return np.asarray(v, dtype=float)


def delta_at(ell: float, eps: float) -> float:
    K, B, f, c = np.eye(2), np.array([[1.0, 0.0]]), np.array([-1.0, 0.0]), np.zeros(1)
    u_hat = np.array([eps, 0.0])
    return float(certify(K, f, B, c, u_hat, np.array([ell]), identity_solve, 1.0).delta)


def run() -> dict:
    K, B, f, c = np.eye(2), np.array([[1.0, 0.0]]), np.array([-1.0, 0.0]), np.zeros(1)
    s1 = MinResidualS1(B, identity_solve)
    out = {"eps": EPSILONS, "error": EPSILONS.copy(), "min_delta": np.zeros_like(EPSILONS), "ell_min": np.zeros_like(EPSILONS),
           "delta_s1": np.zeros_like(EPSILONS), "ell_s1": np.zeros_like(EPSILONS), "closed_form": np.sqrt(EPSILONS * (1 + EPSILONS))}
    for i, eps in enumerate(EPSILONS):
        grid = np.linspace(0.0, 3.0, 3001)
        vals = np.array([delta_at(g, eps) for g in grid])
        k = int(vals.argmin())
        lo, hi = grid[max(k - 1, 0)], grid[min(k + 1, len(grid) - 1)]
        res = minimize_scalar(lambda x: delta_at(x, eps), bounds=(lo, hi), method="bounded", options={"xatol": 1e-14})
        out["min_delta"][i], out["ell_min"][i] = min(res.fun, vals[k]), res.x
        u_hat = np.array([eps, 0.0])
        ell, _ = s1.solve(f - K @ u_hat, np.array([eps]), 1.0)
        out["ell_s1"][i] = float(ell[0])
        out["delta_s1"][i] = delta_at(float(ell[0]), eps)
    return out


def main() -> int:
    setup_logging()
    out = run()
    dev = float(np.max(np.abs(out["min_delta"] - out["closed_form"]) / out["closed_form"]))
    slope = float(np.polyfit(np.log(out["eps"][:12]), np.log(out["min_delta"][:12]), 1)[0])
    summary = {"max_rel_deviation_min_delta_vs_closed_form": dev, "loglog_slope_of_min_delta_eps_le_1e-4": slope,
               "ell_s1_minus_1_over_eps_median": float(np.median((out["ell_s1"] - 1.0) / out["eps"]))}
    LOG.info("%s", summary)
    folder = RESULTS / "e_halfrate"
    folder.mkdir(parents=True, exist_ok=True)
    save_result(folder / "halfrate.npz", out, {"experiment": "e_halfrate", "summary": summary})
    (folder / "halfrate.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    return EXIT_OK


if __name__ == "__main__":
    sys.exit(main())
