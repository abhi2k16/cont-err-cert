"""Generate the figures of E1 and E2 from the saved results (no recomputation).

fig_e1_effectivity: effectivity Delta*/||e||_K versus relative error for R0 and R0s (gap rule), pooled over seeds 0-2;
                    points satisfying 0 <= g^ <= 2g (Cor. 3.5) are drawn in a separate colour; the line eff = 1 is the exact value.
fig_e2_support_floor: certificate versus the lift-off amplitude eps for full S1 and the two restricted supports; dashed lines
                    are the floors sigma_S (median over queries and seeds).
Usage:  python experiments/figures.py
"""

import logging
import sys

import numpy as np

from certcorrect.cli import EXIT_BAD_INPUT, EXIT_OK, setup_logging
from certcorrect.config import RESULTS
from certcorrect.plotting import plt, save_figure, use_style

LOG = logging.getLogger("e_figures")
SEEDS = (0, 1, 2)
PROBLEMS = ("membrane", "block")
E1_KINDS = (("R0", "R0"), ("R0s_gap", "R0s (gap rule)"))
SUPPORTS = (("full", "full S1", "C0"), ("omit_i", r"all rows but $i^*$", "C3"), ("omit_A", r"$A_+$ without $i^*$ (nearly coincides)", "C2"))


def load(experiment: str, problem: str) -> dict:
    parts = [np.load(RESULTS / experiment / f"{problem}_seed{s}.npz", allow_pickle=True) for s in SEEDS]
    return {k: [p[k] for p in parts] for k in parts[0].files if not k.startswith("_")}


def fig_e1() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(6.8, 2.7), sharey=True)
    for ax, problem in zip(axes, PROBLEMS):
        d = load("e1_exactness", problem)
        for (kind, label), marker in zip(E1_KINDS, ("o", "s")):
            err, eff, cond = (np.concatenate(d[f"{k}_{kind}"]) for k in ("error", "eff", "cond"))
            cond = cond.astype(bool)
            ax.loglog(err[~cond], eff[~cond], marker, ms=2.5, alpha=0.4, color="C0" if marker == "o" else "C1",
                      label=f"{label}, (C) fails", rasterized=True)
            ax.loglog(err[cond], eff[cond], marker, ms=2.5, alpha=0.7, color="C2" if marker == "o" else "C3",
                      label=f"{label}, (C) holds", rasterized=True)
        ax.axhline(1.0, color="k", lw=0.8)
        ax.set_title(problem)
        ax.set_xlabel(r"relative error $\|e\|_K/\|u\|_K$")
    axes[0].set_ylabel(r"effectivity $\Delta^\star/\|e\|_K$")
    axes[1].legend(loc="upper right", fontsize=6)
    save_figure(fig, "fig_e1_effectivity")


def fig_e2() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(6.8, 2.7), sharey=True)
    for ax, problem in zip(axes, PROBLEMS):
        d = load("e2_support_floor", problem)
        eps = d["eps"][0]
        for name, label, color in SUPPORTS:
            delta = np.concatenate(d[f"delta_{name}"], axis=0)
            ax.loglog(eps, np.nanmedian(delta, axis=0), "-o" if name != "omit_i" else "-s", color=color, label=label,
                      ms=4 if name != "omit_i" else 7, mfc="none" if name == "omit_i" else None, zorder=3 if name == "omit_A" else 2)
            if name != "full":
                ax.axhline(np.nanmedian(np.concatenate(d[f"sigma_{name}"])), color=color, ls="--", lw=0.9)
        ax.set_title(problem)
        ax.set_xlabel(r"lift-off amplitude $\varepsilon$")
    axes[0].set_ylabel(r"certificate $\Delta^\star$ (median)")
    axes[0].legend(loc="lower right", fontsize=6)
    save_figure(fig, "fig_e2_support_floor")


def fig_halfrate() -> None:
    d = np.load(RESULTS / "e_halfrate" / "halfrate.npz", allow_pickle=True)
    eps = d["eps"]
    fig, ax = plt.subplots(figsize=(3.6, 2.8))
    ax.loglog(eps, d["error"], "-", color="k", label=r"error $\|e\|_K=\varepsilon$")
    ax.loglog(eps, d["min_delta"], "o", ms=3, color="C3", label=r"$\min_{\ell \geq 0}\Delta^\star(\ell)$")
    ax.loglog(eps, d["closed_form"], "-", color="C3", lw=0.8, label=r"$\sqrt{\varepsilon(1+\varepsilon)}$")
    ax.loglog(eps, d["delta_s1"], "s", ms=3, mfc="none", color="C0", label=r"S1 multiplier")
    ax.set_xlabel(r"error $\varepsilon$")
    ax.set_ylabel("certificate")
    ax.legend(loc="lower right", fontsize=6)
    save_figure(fig, "fig_halfrate")


def main() -> int:
    setup_logging()
    use_style()
    try:
        fig_e1(), fig_e2(), fig_halfrate()
    except FileNotFoundError as exc:
        LOG.error("missing result file: %s (run the experiments first)", exc)
        return EXIT_BAD_INPUT
    LOG.info("wrote fig_e1_effectivity, fig_e2_support_floor and fig_halfrate to paper/figures")
    return EXIT_OK


if __name__ == "__main__":
    sys.exit(main())
