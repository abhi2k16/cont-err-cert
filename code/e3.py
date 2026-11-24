"""E3 (archive/SHORT_PAPER_SCOPE.md): property test of the proved statements on random inequality-constrained SPD systems.

Instances: random SPD K, random full-row-rank B, random f, c with a mixture of active and inactive rows; exact solution
from the condensed LCP  D lam + (B u_f - c) >= 0, D = B K^-1 B^T. Feasible approximations u^ of several kinds:
  cover   random perturbation of u, R0-snap on A_+ (consistent: g^_i = 0 on A_+)
  miss    same, snap on a random proper subset of A_+ (strictly active rows left open)
  over    snap on A_+ plus random extra rows
  plain   R0 (no snap)
  exact   X = K only: u^ = u + B^+ t + (null-space part), t_i in [-g_i, g_i]  (so 0 <= g^ <= 2 g: Cor. 3.5 applies)
Inner products: X = K (alpha = gamma = 1) or a random SPD X (alpha, gamma = extreme generalised eigenvalues of (K, X)).

Statements checked (paper numbering, 23 Nov 2026 draft):
  Lem 2.2   Phi <= Delta^2 <= 4/3 Phi (l* and random l >= 0);  Rem 3.2: inexact S1, and no 2/sqrt3 if eta(l*) = 0
  Thm 3.1   ||e||_K <= Delta*(l*) <= (2/sqrt3) (s^2 ||e||^2 + lam.g^)^(1/2);  lam.g^ <= m(A_+) ||e||
  Cor 3.3   lam.g^ = 0  =>  eff <= (2/sqrt3) s
  Prop 2.3  (X = K) J(u^)-J(u) = ||e||^2/2 + lam.g^;  G = rho^2/2 + eta;  Delta* <= sqrt(2G)
  Prop 3.4  (X = K) S1 = LCP with obstacle c + g^/2; rho(l*) = ||u^ - u'||_K; u^ feasible for it, u' for the original
  Cor 3.5   (X = K, 0 <= g^ <= 2 g)  l* = lam and Delta* = ||e||_K
  Thm 3.7   lam.g^ = sum_M lam_i g^_i = -lam_M.B e <= m(M) ||e||;  eff <= (2/sqrt3)(s^2 + m(M)/||e||)^(1/2)
  Cor 3.8   lam.g^ <= ||lam_M||_2 ||g^_M||_2 <= ||lam_M||_1 max_M g^_i
  Thm 3.9   restricted support S: upper bound with m(S^c); lower bound (sigma_S - sqrt(gamma)||e||)/sqrt(alpha); sigma_S > 0 iff A_+ not in S
Criterion (fixed before running): zero violations beyond 1e-9 relative (equalities to 1e-9); observed ratios reported.

Output: results/e3_random/summary.json (per statement: checked, violations, worst margin, ratio statistics).
Usage:  python experiments/e3.py --seed 0 --n-instances 1000
"""

import json
import logging

import numpy as np
import scipy.linalg as sla
import scipy.sparse as sp

from certcorrect import cli
from certcorrect.certificate import certify
from certcorrect.config import RESULTS
from certcorrect.multipliers import MinResidualS1
from certcorrect.rom import solve_complementarity
from certcorrect.theory import support_floor

LOG = logging.getLogger("e3_random_instances")
TOL = 1e-9
ACTIVE_TOL = 1e-10
SQRT3 = np.sqrt(3.0)
KINDS = ("cover", "miss", "over", "plain", "exact")
SIZES = ((8, 3), (15, 5), (30, 8), (50, 12))        # (n, m)
PERTURBATIONS = (1e-1, 1e-2, 1e-3)


class Tally:
    """Counts checks of one statement: violations and the worst margin (negative margin = violation)."""

    def __init__(self):
        self.checked, self.violations, self.worst, self.ratios, self.nontrivial = 0, 0, np.inf, [], 0

    def inequality(self, lhs: float, rhs: float, scale: float) -> None:
        margin = (rhs - lhs) / max(abs(scale), 1e-300)
        self.checked += 1
        self.worst = min(self.worst, margin)
        self.violations += margin < -TOL
        if rhs > 0 and lhs > 0:              # ratio of the two sides; a nonpositive left side is a trivial bound
            self.ratios.append(lhs / rhs)
            self.nontrivial += 1

    def equality(self, lhs: float, rhs: float, scale: float, floor: float = 0.0) -> None:
        """Identity check: |lhs - rhs| <= TOL * scale + floor (``floor`` = rounding estimate of the evaluation)."""
        err = abs(lhs - rhs) / max(abs(scale), 1e-300)
        self.checked += 1
        self.worst = min(self.worst, -err)
        self.violations += abs(lhs - rhs) > TOL * abs(scale) + floor
        if floor > 0:
            self.over_floor = max(getattr(self, "over_floor", 0.0), abs(lhs - rhs) / floor)

    def summary(self) -> dict:
        out = {"checked": self.checked, "violations": int(self.violations), "worst_margin": float(self.worst),
               "nontrivial": self.nontrivial}
        if hasattr(self, "over_floor"):
            out["max_discrepancy_over_rounding_floor"] = float(self.over_floor)
        if self.ratios:
            r = np.array(self.ratios)
            out.update(ratio_min=float(r.min()), ratio_median=float(np.median(r)), ratio_max=float(r.max()))
        return out


def random_spd(rng, n: int) -> np.ndarray:
    a = rng.standard_normal((n, n))
    return a @ a.T + n * np.eye(n)


def exact_solution(K, B, f, c):
    """Exact solution from the condensed LCP, then polished: with the active set A = {lam > 0} identified, the
    equality-constrained KKT system [K -B_A^T; B_A 0] [u; lam_A] = [f; c_A] is solved directly, which removes the
    solver tolerance (KKT residual and complementarity defect ~1e-12) that would otherwise limit identities whose
    sides are O(||e||^2). The polished pair replaces the LCP pair only if it is a valid solution."""
    Ki = np.linalg.inv(K)
    D = B @ Ki @ B.T
    lam, ok = solve_complementarity(0.5 * (D + D.T), B @ Ki @ f - c)
    u = Ki @ (f + B.T @ lam)
    act = np.flatnonzero(lam > 1e-12 * max(lam.max(), 1.0))
    if ok and act.size:
        n, k = K.shape[0], act.size
        system = np.block([[K, -B[act].T], [B[act], np.zeros((k, k))]])
        sol = np.linalg.solve(system, np.concatenate([f, c[act]]))
        u2, lam2 = sol[:n], np.zeros_like(lam)
        lam2[act] = sol[n:]
        if lam2[act].min() > 0 and (B @ u2 - c).min() >= -1e-12 * max(np.abs(c).max(), 1.0):
            lam, u = lam2, u2
    return Ki, D, lam, u, ok


def make_instance(rng, n: int, m: int):
    """Random problem with at least one strictly active and one inactive row (retries)."""
    while True:
        K, B, f = random_spd(rng, n), rng.standard_normal((m, n)), rng.standard_normal(n)
        uf = np.linalg.solve(K, f)
        c = B @ uf + rng.standard_normal(m) * np.abs(B @ uf).mean()
        Ki, D, lam, u, ok = exact_solution(K, B, f, c)
        plus = np.flatnonzero(lam > ACTIVE_TOL * max(lam.max(), 1.0))
        if ok and 1 <= len(plus) < m:
            return K, B, f, c, Ki, D, lam, u, plus


def approximation(rng, kind, K, B, c, u, plus, g, scale, Bp):
    """Feasible u^ of the requested kind."""
    m, n = B.shape
    if kind == "exact":
        t = np.where(g > ACTIVE_TOL, rng.uniform(-1.0, 1.0, m) * g, 0.0)
        w = rng.standard_normal(n)
        null = w - Bp @ (B @ w)
        return u + Bp @ t + 0.3 * scale * np.linalg.norm(u) / np.sqrt(n) * null
    u_t = u + scale * np.linalg.norm(u) / np.sqrt(n) * rng.standard_normal(n)
    gt = B @ u_t - c
    d = np.maximum(-gt, 0.0)
    if kind == "cover":
        snap = plus
    elif kind == "miss":
        snap = plus[rng.random(len(plus)) < 0.5]
        if len(snap) == len(plus):
            snap = plus[:-1]
    elif kind == "over":
        snap = np.union1d(plus, np.flatnonzero(rng.random(m) < 0.3))
    else:
        snap = np.zeros(0, int)
    d[snap] = -gt[snap]
    return u_t + Bp @ d


def check_instance(tallies, rng, kind, same_x, scale, n, m):
    K, B, f, c, Ki, D, lam, u, plus = make_instance(rng, n, m)
    g = B @ u - c
    Bp = B.T @ np.linalg.inv(B @ B.T)
    u_hat = approximation(rng, kind, K, B, c, u, plus, g, scale, Bp)
    g_hat = B @ u_hat - c
    assert g_hat.min() >= -1e-9 * max(np.abs(c).max(), 1.0)
    g_hat = np.maximum(g_hat, 0.0)
    e = u - u_hat
    e_norm = np.sqrt(e @ K @ e)
    if e_norm < 1e-12 * np.sqrt(u @ K @ u):
        return
    if same_x:
        X, alpha, gamma = K, 1.0, 1.0
    else:
        X = random_spd(rng, n)
        ev = sla.eigh(K, X, eigvals_only=True)
        alpha, gamma = float(ev.min()), float(ev.max())
    s2 = gamma / alpha
    Xi = np.linalg.inv(X)
    solve_x = lambda r: Xi @ r                                                    # noqa: E731
    Bs, Ks = sp.csr_matrix(B), sp.csr_matrix(K)
    s1 = MinResidualS1(Bs, solve_x)
    ell, ok = s1.solve(f - K @ u_hat, g_hat, alpha)
    assert ok
    cert = certify(Ks, f, Bs, c, u_hat, ell, solve_x, alpha)
    delta, eta_true = cert.delta, float(lam @ g_hat)
    scale_e = e_norm
    phi_star = cert.rho_bar**2 + cert.complementarity
    # Lemma 2.2 (Phi <= Delta^2 <= 4/3 Phi) for l* and random nonnegative multipliers
    for ell_r in (ell, np.abs(rng.standard_normal(m)) * max(lam.max(), 1e-3), np.maximum(ell + 0.05 * lam.max() * rng.standard_normal(m), 0.0)):
        c_r = certify(Ks, f, Bs, c, u_hat, ell_r, solve_x, alpha)
        phi_r = c_r.rho_bar**2 + c_r.complementarity
        tallies["Lem 2.2 Phi <= Delta^2"].inequality(phi_r, c_r.delta**2, c_r.delta**2)
        tallies["Lem 2.2 Delta^2 <= 4/3 Phi"].inequality(c_r.delta**2, 4.0 / 3.0 * phi_r, c_r.delta**2)
    # Remark 3.2: inexact S1 (Phi(l~) <= Phi(l*) + delta) and the case eta(l*) = 0
    ell_t = np.maximum(ell + 0.02 * lam.max() * rng.standard_normal(m), 0.0)
    c_t = certify(Ks, f, Bs, c, u_hat, ell_t, solve_x, alpha)
    slack = max(c_t.rho_bar**2 + c_t.complementarity - phi_star, 0.0)
    tallies["Rem 3.2 inexact S1"].inequality(
        c_t.delta, (2 / SQRT3) * np.sqrt(s2 * e_norm**2 + eta_true + slack), scale_e)
    if cert.complementarity <= 1e-14 * max(cert.rho_bar**2, 1e-300):
        tallies["Rem 3.2 no 2/sqrt3 if eta(l*)=0"].inequality(delta, np.sqrt(s2 * e_norm**2 + eta_true), scale_e)
    # Theorem 3.1
    tallies["Thm 3.1 lower"].inequality(e_norm, delta, scale_e)
    tallies["Thm 3.1 upper"].inequality(delta, (2 / SQRT3) * np.sqrt(s2 * e_norm**2 + eta_true), scale_e)
    m_plus = np.sqrt(max((B.T @ lam) @ Ki @ (B.T @ lam), 0))
    tallies["Thm 3.1 lam.g <= m(A+)||e||"].inequality(eta_true, m_plus * e_norm, scale_e**2)
    # Corollary 3.3
    miss = np.flatnonzero((lam > ACTIVE_TOL * max(lam.max(), 1.0)) & (g_hat > ACTIVE_TOL * max(np.abs(c).max(), 1.0)))
    if eta_true <= 1e-12 * e_norm**2:
        tallies["Cor 3.3 eff <= 2/sqrt3 s"].inequality(delta / e_norm, (2 / SQRT3) * np.sqrt(s2), 1.0)
    # Theorem 3.7 and Corollary 3.8
    lam_m = np.zeros_like(lam)
    lam_m[miss] = lam[miss]
    m_miss = np.sqrt(max((B.T @ lam_m) @ Ki @ (B.T @ lam_m), 0))
    tallies["Thm 3.7 identity lam.g = -lam_M.Be"].equality(eta_true, -lam_m @ (B @ e), scale_e**2)
    tallies["Thm 3.7 lam.g <= m(M)||e||"].inequality(eta_true, m_miss * e_norm, scale_e**2)
    tallies["Thm 3.7 eff bound"].inequality(delta / e_norm, (2 / SQRT3) * np.sqrt(s2 + m_miss / e_norm), 1.0)
    if len(miss):
        tallies["Cor 3.8 localized"].inequality(eta_true, np.linalg.norm(lam[miss]) * np.linalg.norm(g_hat[miss]),
                                                scale_e**2)
    # Theorem 3.9 with a random support
    for support in (plus, np.sort(rng.choice(m, size=max(1, m // 2), replace=False))):
        ell_s, ok_s = s1.solve(f - K @ u_hat, g_hat, alpha, support)
        d_s = certify(Ks, f, Bs, c, u_hat, ell_s, solve_x, alpha).delta
        outside = np.setdiff1d(np.arange(m), support)
        lam_out = np.zeros_like(lam)
        lam_out[outside] = lam[outside]
        m_out = np.sqrt(max((B.T @ lam_out) @ Ki @ (B.T @ lam_out), 0))
        sigma = support_floor(Bs, lam, support, solve_x)
        tallies["Thm 3.9 upper"].inequality(
            d_s, (2 / SQRT3) * np.sqrt(s2 * (e_norm + m_out) ** 2 + eta_true), scale_e)
        tallies["Thm 3.9 lower (floor)"].inequality((sigma - np.sqrt(gamma) * e_norm) / np.sqrt(alpha), d_s, scale_e)
        covers = np.isin(plus, support).all()
        tallies["Thm 3.9 sigma_S > 0 iff A+ not in S"].checked += 1
        tallies["Thm 3.9 sigma_S > 0 iff A+ not in S"].violations += bool(covers == (sigma > 1e-7 * max(np.sqrt(lam @ lam), 1)))
    if not same_x:
        return
    # X = K statements
    J = lambda v: 0.5 * v @ K @ v - f @ v                                          # noqa: E731
    r = f + B.T @ ell - K @ u_hat
    rho = np.sqrt(max(r @ Ki @ r, 0))
    rhs_energy = 0.5 * e_norm**2 + eta_true
    # counted check: J(u^) - J(u) with u^ = u - e, evaluated in the algebraically identical form that avoids cancellation
    tallies["Prop 2.3 energy identity"].equality(-e @ (K @ u - f) + 0.5 * e_norm**2, rhs_energy, scale_e**2)
    # diagnostic (not counted in TOTAL): the direct difference of two O(||u||^2) numbers, with a rounding allowance
    rounding = 16 * n * np.finfo(float).eps * (abs(J(u_hat)) + abs(J(u)) + abs(f @ u_hat) + abs(f @ u))
    tallies["Prop 2.3 energy identity (direct J difference, diagnostic)"].equality(
        J(u_hat) - J(u), rhs_energy, scale_e**2, floor=rounding)
    gap = 0.5 * rho**2 + float(ell @ g_hat)
    # G = J(u^) - D(l) = rho^2/2 + eta holds algebraically for ANY (u^, l) (no use of the exact solution); the direct difference of two
    # O(||u||^2) numbers is limited by rounding, so the check allows the rounding estimate of the evaluation
    w = f + B.T @ ell
    dual = -0.5 * w @ Ki @ w + ell @ c
    rounding_g = 16 * n * np.finfo(float).eps * (abs(J(u_hat)) + abs(0.5 * w @ Ki @ w) + abs(ell @ c) + abs(f @ u_hat))
    tallies["Prop 2.3 gap identity (up to rounding)"].equality(J(u_hat) - dual, gap, scale_e**2, floor=rounding_g)
    tallies["Prop 2.3 Delta <= sqrt(2G)"].inequality(delta, np.sqrt(2 * gap), scale_e)
    c_shift = c + 0.5 * g_hat
    lam_ref, ok_ref = solve_complementarity(0.5 * (D + D.T), B @ Ki @ f - c_shift)
    u_prime = Ki @ (f + B.T @ ell)
    tallies["Prop 3.4 S1 = shifted LCP"].equality(np.linalg.norm(ell - lam_ref), 0.0, max(np.linalg.norm(lam), 1e-300))
    tallies["Prop 3.4 rho = ||u^-u'||_K"].equality(rho, np.sqrt((u_hat - u_prime) @ K @ (u_hat - u_prime)), scale_e)
    feas = min((B @ u_hat - c_shift).min(), (B @ u_prime - c).min())
    tallies["Prop 3.4 feasibility"].inequality(0.0, feas + 1e-9 * max(np.abs(c).max(), 1.0), 1.0)
    if (g_hat >= -1e-12).all() and (g_hat <= 2 * g + 1e-12).all() and not np.any((g <= ACTIVE_TOL) & (g_hat > 1e-12)):
        tallies["Cor 3.5 Delta = ||e|| (0<=g^<=2g)"].equality(delta, e_norm, scale_e)
        tallies["Cor 3.5 l* = lam"].equality(np.linalg.norm(ell - lam), 0.0, max(np.linalg.norm(lam), 1e-300))


STATEMENTS = ("Lem 2.2 Phi <= Delta^2", "Lem 2.2 Delta^2 <= 4/3 Phi", "Rem 3.2 inexact S1",
              "Rem 3.2 no 2/sqrt3 if eta(l*)=0", "Thm 3.1 lower", "Thm 3.1 upper", "Thm 3.1 lam.g <= m(A+)||e||", "Cor 3.3 eff <= 2/sqrt3 s",
              "Thm 3.7 identity lam.g = -lam_M.Be", "Thm 3.7 lam.g <= m(M)||e||", "Thm 3.7 eff bound",
              "Cor 3.8 localized", "Thm 3.9 upper", "Thm 3.9 lower (floor)", "Thm 3.9 sigma_S > 0 iff A+ not in S",
              "Prop 2.3 energy identity", "Prop 2.3 energy identity (direct J difference, diagnostic)",
              "Prop 2.3 gap identity (up to rounding)", "Prop 2.3 Delta <= sqrt(2G)",
              "Prop 3.4 S1 = shifted LCP", "Prop 3.4 rho = ||u^-u'||_K", "Prop 3.4 feasibility",
              "Cor 3.5 Delta = ||e|| (0<=g^<=2g)", "Cor 3.5 l* = lam")


def main(args) -> int:
    path = RESULTS / "e3_random" / f"summary_seed{args.seed}.json"
    LOG.info("%d instances, sizes %s -> %s", args.n_instances, SIZES, path)
    if args.dry_run:
        return cli.EXIT_OK
    rng = np.random.default_rng(args.seed)
    tallies = {name: Tally() for name in STATEMENTS}
    counts = {k: 0 for k in KINDS}
    for i in range(args.n_instances):
        kind = KINDS[i % len(KINDS)]
        n, m = SIZES[(i // len(KINDS)) % len(SIZES)]
        same_x = kind == "exact" or rng.random() < 0.5                 # Cor. 3.5 needs X = K
        check_instance(tallies, rng, kind, same_x, PERTURBATIONS[(i // 7) % len(PERTURBATIONS)], n, m)
        counts[kind] += 1
    summary = {name: t.summary() for name, t in tallies.items()}
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({"seed": args.seed, "n_instances": args.n_instances, "kinds": counts, "tol": TOL,
                                "statements": summary}, indent=2), encoding="utf-8")
    total_v = sum(s["violations"] for name, s in summary.items() if "diagnostic" not in name)
    diag_v = sum(s["violations"] for name, s in summary.items() if "diagnostic" in name)
    for name, s in summary.items():
        ratio = (f"ratio lhs/rhs median {s['ratio_median']:.3f} (min {s['ratio_min']:.3f}, max {s['ratio_max']:.3f}, "
                 f"nontrivial {s['nontrivial']})") if "ratio_median" in s else "equality / identity"
        LOG.info("%-40s checked %5d | violations %d | worst margin %+.1e | %s", name, s["checked"], s["violations"],
                 s["worst_margin"], ratio)
    LOG.info("TOTAL violations: %d (diagnostic entries: %d)", total_v, diag_v)
    return cli.EXIT_OK if total_v == 0 else cli.EXIT_FAILURE


def parser():
    p = cli.base_parser(__doc__.splitlines()[0])
    p.add_argument("--n-instances", type=int, default=1000)
    return p


if __name__ == "__main__":
    cli.run(main, parser())
