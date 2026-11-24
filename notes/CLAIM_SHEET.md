# Claim sheet for the originality audit of the certificate theory

> **Audit completed 23 Nov 2026: results in CLAIM_SHEET_AUDIT_RESULTS.md** (decision rule formally satisfied, with qualifications). The matrix in Sec. 3 below is the pre-audit state.

Prepared 23 Nov 2026 (CONTACT_RESPONSE_PLAN.md, Sec. 5, "Next"). Purpose: make the full-text audit a mechanical,
claim-by-claim comparison. Statements are those of the paper draft (`certified-correction-contact-rom/paper/`,
Sections 2–4); proofs in ANALYSIS_T1_T3.md and THEOREM_certificate_efficiency.md.

## 0. Common setting and notation

Discrete frictionless contact: $Ku-B^T\lambda=f$, $g=Bu-c\ge0$, $\lambda\ge0$, $\lambda^Tg=0$; $K\succ0$, $B$ full row
rank. Feasible approximation $\hat u$ ($\hat g=B\hat u-c\ge0$), error $e=u-\hat u$. Inner product $X$ with
$\alpha_XX\preceq K\preceq\gamma_XX$, $s^2=\gamma_X/\alpha_X$. Certificate for $\ell\ge0$:
$\Delta^\star(\ell)=\tfrac12(\bar\rho+\sqrt{\bar\rho^2+4\ell^T\hat g})$, $\bar\rho=\|f+B^T\ell-K\hat u\|_{X^{-1}}/\sqrt{\alpha_X}$;
surrogate $\Phi(\ell)=\bar\rho^2+\ell^T\hat g$, minimiser $\ell^\star$ (S1). $\mathcal A_+=\{i:\lambda_i>0\}$.
$m(\mathcal M)=\|B^T\lambda_{\mathcal M}\|_{K^{-1}}$.

The continuous analogue (for translating statements in FE papers): $u_h\leftrightarrow\hat u$, obstacle $\psi$ or gap
function $\leftrightarrow c$, discrete/continuous contact force or $\sigma_n$ $\leftrightarrow\lambda$, contact set
$\{u=\psi\}$ $\leftrightarrow\{g_i=0\}$, $\langle\lambda,u_h-\psi\rangle\leftrightarrow\lambda^T\hat g$.

## 1. Already attributed (not claimed; for completeness)

| Item | Statement | Source (verified) |
|---|---|---|
| K1 | $\|e\|_K\le\Delta^\star(\ell)$ for feasible $\hat u$, $\ell\ge0$ | Zhang–Bader–Veroy 2016, Prop. 4.3; Zhang 2016 (diss.), Prop. 3.3.6 |
| K2 | $\Phi\le\Delta^{\star2}\le\frac43\Phi$ | Zhang 2016 (diss.), Prop. 3.4.1 |
| K3 | S1 (minimum-residual multiplier) | Zhang 2016 (diss.), (3.123)–(3.124) |
| K4 | $J(\hat u)-J(u)=\frac12\|e\|_K^2+\lambda^T\hat g$; gap identity $J(\hat u)-D(\ell)$ | Bartels–Gudi–Kaltenbach 2025, Lemma 4.3(i), Thm. 4.5 (continuous, scalar Signorini; arXiv numbering) |
| K5 | square-root gap between upper and lower bounds observed | Haasdonk–Salomon–Wohlmuth 2012, Remark 4.5 |
| K6 | Falk-type a priori estimate, nested-space monotonicity of $J$ | classical |

## 2. Candidate claims

Risk = prior probability that the claim (or an equivalent) is already published, given what has been read so far.

### A1 — Efficiency of the optimised certificate (paper Theorem 3.1)
**Statement.** For every feasible $\hat u$: $\|e\|_K\le\Delta^\star(\ell^\star)\le\frac{2}{\sqrt3}\big(s^2\|e\|_K^2+\lambda^T\hat g\big)^{1/2}$, and
$\lambda^T\hat g\le m(\mathcal A_+)\|e\|_K$. Inexact S1 ($\Phi(\tilde\ell)\le\Phi(\ell^\star)+\delta$): add $\delta$ inside (Remark 3.2).
**Proof idea.** K1, K2, then $\Phi(\ell^\star)\le\Phi(\lambda)$ and $\bar\rho(\lambda)=\|Ke\|_{X^{-1}}/\sqrt{\alpha_X}\le s\|e\|_K$.
**New part.** Step 3: comparison of the *optimised, computable* certificate with the exact multiplier, giving an
upper bound by the primal error plus $\lambda^T\hat g$ only (no dual error term).
**Counts as known if a source states any of:** (a) an estimator of feasible-pair / quadratic-root / gap type with an
optimised or minimum-residual multiplier is bounded by $C(\|e\|+\sqrt{\langle\lambda,u_h-\psi\rangle})$ or equivalent;
(b) "efficiency up to the complementarity of the exact contact force with the discrete gap"; (c) for gap estimators
$\inf_y\eta^2_{gap}(v,y)=I(v)-I(u)$ written as an efficiency statement (BGK Thm. 4.5 implies this; check whether stated).
**Risk: medium–high** (very close to K4; the novelty is narrow: computability + constant $2/\sqrt3$).

### A2 — Active-set consistency gives uniform efficiency (Corollary 3.2(b),(c))
**Statement.** If $\hat g_i=0$ for all $i\in\mathcal A_+$, then $1\le\Delta^\star(\ell^\star)/\|e\|_K\le\frac{2}{\sqrt3}s$ (for $X=K$: $\le1.155$); if
$\lambda^T\hat g\le C\|e\|_K^2$, then $\le\frac{2}{\sqrt3}(s^2+C)^{1/2}$.
**Counts as known if:** a source states efficiency of a contact-term estimator *conditionally* on the discrete contact
set containing the exact (strict) contact set, or that contact contributions vanish/are higher order under such a
condition (e.g. Krause–Veeser–Walloth: terms "vanish in full contact" — check whether a general consistency condition is
formulated); or Ashby–Pryer-type conditions on the discrete contact set used for efficiency.
**Risk: medium.**

### A3 — The half rate is attained for every multiplier (Proposition 3.3)
**Statement.** $N=2$, $n_c=1$, $K=I$, $B=[1\ 0]$, $c=0$, $f=(-1,0)^T$, $X=K$, $\hat u=(\varepsilon,0)^T$:
$\min_{\ell\ge0}\Delta^\star(\ell)=\sqrt{\varepsilon(1+\varepsilon)}$ (at $\ell=1+\varepsilon$), so $\min_\ell\Delta^\star/\|e\|_K=((1+\varepsilon)/\varepsilon)^{1/2}\to\infty$.
**Counts as known if:** an example or theorem shows that residual-plus-complementarity (or gap) estimators for
obstacle/contact problems lose a square root *for every choice of the dual variable*, when the approximation is open
on part of the exact contact set; (HSW 2012 only observes the gap, K5). Look in Braess 2005, Veeser 2001
(lower bounds), BGK 2025 (rate of $\eta_B$), Nochetto–Siebert–Veeser 2003.
**Risk: medium.**

### A4 — Missed rows (Theorem 3.4) and localized form (Corollary 3.5)
**Statement.** $\mathcal M=\{i\in\mathcal A_+:\hat g_i>0\}$: $\lambda^T\hat g=\sum_{\mathcal M}\lambda_i\hat g_i=-\lambda_{\mathcal M}^TBe\le m(\mathcal M)\|e\|_K$; effectivity
$\le\frac{2}{\sqrt3}(s+\sqrt{m(\mathcal M)/\|e\|_K})$; $\lambda^T\hat g\le\|\lambda_{\mathcal M}\|_1\max_{\mathcal M}\hat g_i$, hence an upper rate $(1+a)/2$ if
$\|\lambda_{\mathcal M}\|_1\lesssim\|e\|^a$ (upper rate only).
**Counts as known if:** a source localises the complementarity defect to "points in the exact contact set where the
approximation is not in contact" and bounds it by the contact force there; or derives intermediate rates from the
decay of the force on such points.
**Risk: medium–low** (elementary, but the specific localisation may not be stated).

### A5 — Restricted multiplier support: bound and floor (Theorem 3.6)
**Statement.** S1 restricted to support $S$: $\Delta^\star(\ell^\star_S)\le\frac{2}{\sqrt3}(s^2(\|e\|_K+m(S^c))^2+\lambda^T\hat g)^{1/2}$ and
$\Delta^\star(\ell^\star_S)\ge(\sigma_S-\sqrt{\gamma_X}\|e\|_K)/\sqrt{\alpha_X}$, $\sigma_S=\min_v\|B^T\lambda_{S^c}-B_S^Tv\|_{X^{-1}}>0$ iff $\mathcal A_+\not\subseteq S$ (fixed problem
and support: certificate does not converge).
**Counts as known if:** RB/VI bounds state that a reduced dual space (cone) that cannot represent the exact multiplier
produces a non-vanishing estimator term — HSW 2012 bounds contain dual-error terms $\|\lambda-\lambda_N\|$, which is
closely related (check Prop. 4.2/4.4 and their discussion); also Burkovska et al. 2015, Benaceur et al. 2020 (dual cone).
**Risk: high** for the floor in spirit (dual approximation error is a known obstruction); the specific support-rule
statement may still be new but is minor.

### A6 — Snapping restores consistency; cost of snapping (Propositions 4.1, 4.3; Corollary 4.4)
**Statement.** Snap correction $\hat u=\tilde u+B^+d$ with $\hat g_i=0$ on $\hat{\mathcal A}$: full rate if $\mathcal A_+\subseteq\hat{\mathcal A}$; exact
identity $\hat u_{snap}=\hat u_{R0}-B^+p$, $p=\tilde g^+$ on $\hat{\mathcal A}$; gap rule bounds the cost by $\beta t|\hat{\mathcal A}_t|^{1/2}$ and gives $M=\emptyset$
if $\|B\tilde e\|_\infty\le t$.
**Counts as known if:** a post-processing that projects an approximate (FE or reduced) solution onto a predicted
contact set to restore estimator efficiency is published, with an accuracy-cost analysis.
**Risk: low–medium** for novelty, but **low value** after D12–D14 (consistent producers such as constrained Galerkin
dominate in practice). Keep only as an explanatory result.

### A7 — Relation to the primal–dual gap (Proposition 2.3)
**Statement.** For $X=K$: $G(\hat u,\ell)=\frac12\bar\rho^2+\ell^T\hat g$ and $\|e\|_K\le\Delta^\star(\ell)\le\sqrt{2G}$, equality iff $\ell^T\hat g=0$.
**Counts as known if:** the inequality between the quadratic-root certificate and the gap is stated (the identities are
K4). **Risk: high / value: low** (two lines of algebra). Not a contribution; a remark.

## 3. Source × claim audit matrix

Legend: **R** read in full (journal version) · **r** read in part / other version · **a** abstract only · **–** not
read. Fill each cell with: *contained* (cite location) / *equivalent* (explain) / *related* / *not found*.

| Source | Version read | A1 | A2 | A3 | A4 | A5 | A6 | A7 |
|---|---|---|---|---|---|---|---|---|
| Haasdonk–Salomon–Wohlmuth 2012 (SINUM) | r (Sec. 4) | not found | not found | related (K5) | not found | **check dual-error terms** | not found | not found |
| Zhang–Bader–Veroy 2016 (C. R. Math.) | r | not found | not found | not found | not found | not found | not found | not found |
| Zhang 2016 (dissertation) | r (Ch. 3–4, 6) | not found | not found | not found | not found | not found | not found | not found |
| S. Zhang 2020 (SISC) | r (first part, arXiv) | related | not found | not found | not found | not found | not found | related |
| Bartels–Gudi–Kaltenbach 2025 (SINUM) | r (arXiv v1, Secs. 1–5) | **check** | **check** | **check** | – | – | not found | **contained (identities)** |
| Ashby–Pryer 2024 (SINUM) | r (arXiv v1, Secs. 1–4.1) | not found | related (Cond. (a_h)) | not found | – | – | not found | – |
| Krause–Veeser–Walloth 2015 (Numer. Math.) | – | – | – | – | – | – | – | – |
| Veeser 2001 (SINUM) | – | – | – | – | – | – | – | – |
| Braess 2005 (Numer. Math.) | – | – | – | – | – | – | – | – |
| Weiss–Wohlmuth 2010 (SISC) | – | – | – | – | – | – | – | – |
| Nochetto–Siebert–Veeser 2003 (Numer. Math.) | – | – | – | – | – | – | – | – |
| Burkovska et al. 2015 (SIFIN) | – | – | – | – | – | – | – | – |
| Benaceur–Ern–Ehrlacher 2020 (IJNME) | a | – | – | – | – | – | – | – |

## 4. Procedure and decision rule

1. For each unread source, read the estimator definition, the reliability and efficiency theorems, and every remark on
   the contact set / complementarity term; fill the row with locations (theorem/equation numbers of the journal version).
2. A claim survives if every row is *not found* or *related* (with the difference statable in one sentence).
3. Decision (fixed now): a focused analysis paper is scoped only if **A1 survives together with at least one of A2,
   A3** (the efficiency–consistency–half-rate core). A4–A7 alone do not justify a paper. If the core does not
   survive, the work is closed as validated infrastructure and documented negative results.

## 5. Inputs needed from the author

Full texts (journal versions), in `literature/`: Krause–Veeser–Walloth 2015; Bartels–Gudi–Kaltenbach 2025;
Veeser 2001; Braess 2005; Weiss–Wohlmuth 2010; optional: Nochetto–Siebert–Veeser 2003, Ashby–Pryer 2024,
Burkovska et al. 2015, Benaceur–Ern–Ehrlacher 2020, Haasdonk–Salomon–Wohlmuth 2012 (to re-check A5).
