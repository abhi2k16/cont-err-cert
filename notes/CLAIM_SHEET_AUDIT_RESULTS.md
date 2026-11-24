# Audit results for CLAIM_SHEET.md (23 Nov 2026)

Texts: the PDFs in `literatures/` (extracted with `pdftotext` to `literatures/text/`). Formulas are partly garbled by the
extraction, so statements below rely on the surrounding text and on structure; exact constants are not asserted.

**Versions read.** Journal versions: Krause–Veeser–Walloth 2015 (KVW), Veeser 2001, Braess 2005, Weiss–Wohlmuth 2010
(WW), Nochetto–Siebert–Veeser 2003 (NSV), Benaceur–Ern–Ehrlacher 2020. **Preprint versions** (journal numbering and
text may differ): Bartels–Gudi–Kaltenbach 2025 (BGK; arXiv v1), Haasdonk–Salomon–Wohlmuth 2012 (HSW; Stuttgart
preprint, May 2011), Burkovska et al. 2015 (arXiv v1), Ashby–Pryer 2024 (preprint). Zhang's dissertation read in the
relevant chapters. Zhang–Bader–Veroy 2016 was not in the folder (its content is in the dissertation).

## 1. What each source contains that is relevant

| Source | Relevant content (location) | Measured error / setting |
|---|---|---|
| **Braess 2005** | Lemma 1, eq. (3.1): $\|u-u_h\|\le\|z-u_h\|+\|\lambda^{ce}\|+(\lambda_h^+,u_h-\psi)^{1/2}$, proved by $x^2\le ax+b\Rightarrow x\le a+\sqrt b$ with $\lambda\ge0$ and $\langle\lambda,u-\psi\rangle=0$: **the FE form of the feasible-pair certificate (K1)**. Remark 1: the complementarity term involves only elements with some, but not all, nodes in the contact area; labelled a higher-order extra term. Corollary 1 and Theorem 1: bound for $\|u-u_h\|+\|\lambda-\lambda_h\|_{-1}$. Sec. 4: efficiency with respect to the same combined error. | FE obstacle; error = primal + multiplier |
| **Veeser 2001** | Thms 3.1, 3.2, 4.1: reliability and local efficiency for $\|u_h-u\|+\|\lambda_h(u_h)-\lambda(u)\|_*$. Remark 3.2: the dual term is a "weak distance" between the discrete and exact contact sets; stated to be new. | FE obstacle; error = primal + contact-set distance |
| **KVW 2015** | Error measure (21): $\|u-u_m\|_1+\|\lambda-\tilde\lambda_m\|_{-1}$. The estimator contains the **complementarity residual** $\eta_6=(\sum s_pd_p)^{1/2}$ (22). Reliability proof, Sec. 4.2, (25) and (32): the cross term $\langle\tilde\lambda_m-\lambda,u-u_m\rangle\le\eta_6^2$, so $\|u-u_m\|^2\le\|G_m\|^2+2\eta_6^2$ (same structure as ours). Thm 2 / Sec. 5.2: lower bound for $\eta_6$ in terms of the combined error under a mesh assumption on semi-contact nodes; **no** lower bounds for $\eta_7,\eta_8$ (obstacle approximation, constraint violation). Abstract and Sec. 1: contact terms vanish for "full" discrete contact (contact on the patch with compatible stress sign). Sec. 1: sharpness "hinges on the approximate Lagrange multiplier" (qualitative). | FE Signorini; error = primal + multiplier |
| **Weiss–Wohlmuth 2010** | Thms 3.2, 3.4: $\|u-u_h\|_a\le C(\eta+\theta_C+\dots)$, with $\theta_C$ "result[ing] from the variational inequality". Thm 3.7 and Remarks 3.5, 3.6: the term need not be considered inside the discrete actual contact zone, only near its boundary; asymptotically negligible (numerical observation). | FE obstacle, primal error |
| **NSV 2003** | Props 6.2, 6.3: efficiency of $\|(u_h-\psi)^+\|$ in pointwise norms, with the multiplier error in the lower bound. | FE obstacle, $L^\infty$ |
| **BGK 2025 (arXiv v1)** | Lemma 4.3(i): $I(v)-I(u)=\frac12\|\nabla(v-u)\|^2+\langle z\cdot n,v-\chi\rangle_{\Gamma_C}-\langle g,v-\chi\rangle_{\Gamma_N}$. Thm 4.5: gap identity (primal plus dual energy excess) for arbitrary conforming $(v,y)$. Thm 6.6: a priori identity for interpolants. No efficiency statement for a feasible-pair certificate; no rate or consistency discussion. | continuous scalar Signorini; energy identities |
| **HSW (2011 preprint)** | Prop. 4.2, (4.13): quadratic-root upper bound $c_1+\sqrt{c_1^2+c_2}$ with a complementarity-type term $s_2$ (RB multiplier, not optimised; $u_N$ not assumed feasible). Prop. 4.4, (4.15)–(4.17): residual $\le$ primal + dual error; $s_2\lesssim\|u-u_N\|$ (constants involve a bound on the RB multiplier and $C/c$). Remark 4.5: the square-root gap is noted. Remark 4.6: dependence on constants. Together: the estimator is at worst $O(\|e\|^{1/2})$. No example attaining it; no closing condition. | RB, variational inequality |
| **Zhang 2016 (diss.)** | Prop. 3.4.1 (3.121): surrogate vs $\Delta^2$ with factor $\frac43$ (K2). (3.123)–(3.124): S1 (K3). Prop. 3.3.5: a priori quasi-optimality of the slack solution "up to the order $O(1/2)$". "Sharp bounds that mimic the convergence rate" is announced and shown numerically (Ch. 4). No bound in terms of the true error. | RB, slack |
| **Ashby–Pryer 2024** | $L^p$ residual-type upper bounds; Condition (a_h) on the discrete contact set (regularity of the dual problem), not an efficiency or consistency condition. | FE Signorini |
| **Burkovska 2015** | Thm 4.2: time-dependent estimator with a projected-slack term; effectivities of two orders of magnitude, numerical (Sec. 6.3.3). | RB, parabolic VI |
| **Benaceur et al. 2020** | No a posteriori bound (cites Zhang–Bader–Veroy and HSW for it). | RB contact |

## 2. Verdicts

| Claim | Verdict | One-sentence difference from the closest source |
|---|---|---|
| **A1** efficiency of the optimised certificate | **not contained; closely anticipated in spirit** | Veeser/Braess/KVW show efficiency only for the primal error *plus* the multiplier (contact-set) error and for estimators built from a discrete multiplier; HSW gives $O(\|e\|^{1/2})$ for a fixed RB multiplier; BGK gives the energy identity. Not found: the *computable optimised-multiplier* certificate bounded by the primal error and the exact-multiplier complementarity $\lambda^T\hat g$ alone, with constant $2/\sqrt3$. Elementary given K2 and the identity; the contribution is the combination. |
| **A2** consistency gives uniform effectivity | **not contained; related** | KVW, WW and Braess show that contact-related *estimator terms* vanish for full discrete contact or inside the discrete contact zone and are localised to its boundary (FE, discrete complementarity); none states an effectivity bound $\le\frac{2}{\sqrt3}s$ under $\hat g_i=0$ on the exact strictly active set, nor a rate. |
| **A3** half rate for every multiplier | **not found** | HSW Remark 4.5 and Zhang Prop. 3.3.5 note the square-root phenomenon; no example, no optimum over all multipliers, no statement that it is unavoidable. |
| **A4** missed rows, localised form | **not found; related localisation** | Braess Remark 1 and WW Thm 3.7 localise the contact-related term to the free boundary of the discrete contact zone; no force-weighted bound and no intermediate rates. |
| **A5** support floor of a restricted multiplier | **not found; related** | HSW (4.15) has the dual error in the lower bound; Veeser and KVW count the multiplier error in the measured error; none states a floor of the certificate for a fixed restricted multiplier space. |
| **A6** snapping and its cost | **not found** (low value after D12–D14) | none |
| **A7** certificate $\le\sqrt{2\cdot\text{gap}}$ | **identities contained** (BGK Lemma 4.3, Thm 4.5; discrete vector form here); inequality elementary | a remark, not a contribution |
| K1 (feasible-pair certificate) | already attributed; **FE analogue also in Braess 2005, Lemma 1, and KVW Sec. 4.2** | add to the attribution |

## 3. Decision rule (fixed in CLAIM_SHEET.md, Sec. 4, before the audit) and outcome

Rule: a focused analysis paper is scoped only if A1 survives together with at least one of A2, A3.

**Outcome: the rule is formally satisfied** (A1: not contained, difference statable in one sentence; A2: not contained,
related; A3: not found).

**Honest qualification.** The surviving content is narrow and mostly elementary algebra on top of known results (K1, K2,
and the BGK/Falk energy identities). The *phenomenon* that efficiency requires counting the contact-set mismatch or the
multiplier error is known since Veeser 2001. What is not found is its precise form for feasible-pair certificates of
(reduced) discrete contact problems:
1. the exact quantity $\lambda^T\hat g$ and the $2/\sqrt3$ bound for the optimised multiplier (A1);
2. the consistency condition with effectivity $\le\frac{2}{\sqrt3}s$ (A2);
3. the explicit example with optimum $\sqrt{\varepsilon(1+\varepsilon)}$ for all multipliers (A3).

**Limits of this audit.** The preprint versions listed above; extraction-garbled formulas (e.g. the exact constants in HSW
(4.17) were not read); and no search beyond the supplied papers (Chen–Nochetto, cited by Veeser and Braess, and
Repin-type functional a posteriori estimates were not read). The audit establishes absence from these sources, not
absence from the literature.

## 4. Consequences for the manuscript text

- Intro and Sec. 3 must say that FE efficiency results measure the error as primal **plus** multiplier error, and must
  cite Braess 2005 (Lemma 1) and KVW (Sec. 4.2) as FE analogues of the certificate mechanism.
- The statement "to our knowledge, not contained in [...]" now has an explicit source list; the open \verify tags
  concern only the journal versions of BGK, HSW, Burkovska et al. and Ashby–Pryer.

---

# Addendum (23 Nov 2026): external verification report, S1 as a contact problem, Repin-Valdman

## A. Verification of the external report's new claim: S1 is a shifted contact problem

For $X=K$ ($\alpha_X=1$): $\nabla\Phi(\ell)=2(D\ell+Bu_f-c-\tfrac12\hat g)$ with $D=BK^{-1}B^T$, $u_f=K^{-1}f$, so the S1
minimiser is the exact multiplier of the contact problem with obstacle $c'=c+\hat g/2$. **Verified** (paper Proposition 3.4):
proof by algebra; numerically against the engine's own contact solver on the shifted obstacle (membrane, four corrections;
multiplier and displacement agree to $10^{-15}$; $\bar\rho(\ell^\star)=\|\hat u-u'\|_K$ exactly; $\hat u$ feasible for
the shifted problem, $u'$ for the original), and by unit test `test_s1_is_the_contact_problem_with_shifted_obstacle`.
The report's reading (S1 costs about one condensed contact solve) was already in MATH_FORMULATION_v6c.md, Remark 2.

## B. A consequence the report does not draw (new, proved and tested)

If $X=K$ and $0\le\hat g\le2g$ componentwise, then $(u,\lambda)$ solves the shifted problem, so $\ell^\star=\lambda$, $u'=u$ and
$\Delta^\star(\ell^\star)=\|e\|_K$: **effectivity exactly 1** (paper Corollary 3.5; test
`test_exact_certification_when_gap_is_between_zero_and_twice_the_true_gap`, which also checks that the identity fails when an
active row is left open). This sharpens Corollary 3.3(b) ($\le2/\sqrt3$) for $X=K$ and is consistent with the effectivities 1.00
observed for corrections covering the strictly active set. The half-rate example violates the condition ($\hat g=\varepsilon>0=g$).
For a restricted support $S$, S1 is the shifted problem with only the constraints in $S$ enforced; omitting a strictly active row gives
$u'_S\ne u$ (injectivity of $B^T$), which is the mechanism behind the certificate floor (A5).

## C. Limit of the half-rate claim A3 (diagnostic, not in the paper)

The half rate is a property of the feasible-pair certificate class $\Delta^\star(\ell)$, not of the problem. From
$u'=t+P_C(u_f-t)$, $t=R\,\hat g_J/2$ (translation of the feasible set; any right inverse $R$) one gets, for a row set $J$ containing the contact
sets of $u$ and $u'$, $\|u-u'\|_K\le\|\hat g_J\|_{D_{JJ}^{-1}}$ and hence the linear bound $\|e\|_K\le\bar\rho(\ell^\star)+\|\hat g_J\|_{D_{JJ}^{-1}}$. In the half-rate
example this gives $1.5\varepsilon$. But it needs the unknown contact set: with all rows the bound is $O(1)$ (measured 3.5-4.1 against $\|e\|\approx0.02$-$0.5$),
with the oracle $J$ it equals the error to rounding. So no computable linear certificate follows; the statement "no multiplier restores the
full rate" stays true within the feasible-pair class and is worst-case. Whether the contact set can be certified computably is open.

## D. Repin-Valdman 2018 and the Repin references

- **Repin, Valdman, "Error identities for variational problems with obstacles", ZAMM 98(4) 635-658 (2018), doi
  10.1002/zamm.201700105: verified on Crossref (journal article).** Read: arXiv 1702.08689 v1, Secs. 1-2.3 verbatim (rest only
  summarised, not relied on). Contents: Thm 1 (29): $\mathbb M(u,v)=\frac12\|\nabla(u-v)\|_A^2+\mu_{\varphi\psi}(v)=J(v)-J(u)$ with $\mu$ a contact term
  integrating the residual against the gap on the exact contact sets; Thm 2 (32): identity for the duality gap with a further contact term; (27): $\mu=0$ when the
  exact contact sets lie inside the approximate ones; Remark 3: simplified equality when the dual contact set lies inside the primal one; abstract: the contact term
  "may serve as an indicator that the free boundaries are approximated very roughly".
  **Consequence: the continuous, identity-level form of A2 (and part of A4) and of our energy identity is in Repin-Valdman 2018, earlier than BGK 2025.**
  Not visible/read: whether a majorant minimised over the dual variable is bounded by the primal error alone (A1); any square-root or rate statement (A3).
- Repin, "Estimates of deviations from exact solutions of elliptic variational inequalities", J. Math. Sci. 115(6) 2811-2819 (2003), and "Functional a posteriori
  estimates for elliptic variational inequalities", J. Math. Sci. 152(5) 702-712 (2008): exist (Crossref), **paywalled, not read**. Repin's book (de Gruyter 2008): no
  chapter title on obstacle problems; contents not read.

## E. Updated verdicts and decision

- A2: identity-level content anticipated (Repin-Valdman, BGK, KVW, WW); certificate-level exactness (Cor. 3.5, eff = 1 for $X=K$) and the $\le\frac{2}{\sqrt3}s$ bound not found.
- A1, A3: still not found in any text read; the Repin majorant papers of 2003/2008 are the remaining unverified source.
- The pre-registered rule (A1 with A2 or A3) remains formally satisfied, on a thinner evidence base than stated in Sec. 3 above: the Repin check is incomplete.
- The external report's conclusion (retain the theory, finish the functional-majorant check, then decide) is adopted; the new results B and the S1 equivalence
  strengthen the analysis but do not change the novelty risk, since they are short consequences of KKT conditions.

---

# Addendum F (23 Nov 2026): Repin 2000 and 2007 read in full text

**Access.** The links in the review returned the Math-Net landing page (HTML, 26 kB), not the PDF. The landing page's own full-text link
(`/php/getFT.phtml?jrnid=znsl&paperid=65|1356&what=fullt`) delivered both PDFs (English text), now in `literatures/`. Texts are partly garbled by
extraction; the equations quoted below were checked against the surrounding text. These are the original POMI Zapiski versions; the
J. Math. Sci. translations (2003, 2008) were verified on Crossref only.

**Repin 2007 (POMI 348; J. Math. Sci. 152(5), 2008), Sec. 2** — the review's description is confirmed. (2.12): for $v\in K$, any $y\in H(\mathrm{div})$ and
**arbitrary nonnegative functions** $\lambda_1,\lambda_2$,
$\|\nabla(u-v)\|^2\le\big[C\|f+\mathrm{div}\,y+\lambda_1-\lambda_2\|+\|y-A\nabla v\|\big]\|\nabla(u-v)\|+\int(\lambda_1(v-\varphi)+\lambda_2(\psi-v))\,dx$;
(2.13): its quadratic-root solution (residual $M$ plus the square root of the complementarity integral), i.e. **the functional form of the feasible-pair certificate
$\Delta^\star(\ell)=\frac12(\bar\rho+\sqrt{\bar\rho^2+4\ell^T\hat g})$**. (2.14)–(2.23): the weighted (Young) version is **minimised over the nonnegative multipliers, pointwise and in
closed form** — the continuous analogue of S1. Theorem 2.1: the majorant is zero iff $v=u$ and $y=A\nabla u$ (analogue of our Lemma 2).
**Repin 2000 (POMI 271; J. Math. Sci. 115(6), 2003), Sec. 2:** Propositions 1–2: majorants $M_1\ge M_2$ vanish iff $v=u$, $\sigma=A\nabla u$; (2.23)–(2.24): the
multiplier minimisation done exactly (explicit piecewise integrand $R$); Remark 1: $M_2\to0$ if $v_k\to u$ and $\sigma_k\to A\nabla u$ (qualitative continuity, no rate);
Remark 3: optimal majorant requires minimisation over the free parameters. "Perturbed problem" (Sec. 2.2) is the perturbation of the *functional* of duality
theory, **not a shifted obstacle**; so the review's phrase "perturbed obstacle problems" does not correspond to our Proposition 3.4.

**Not found in either paper:** any bound of the minimised majorant by the true error (efficiency/effectivity or rate), any condition on the contact set for such a bound, an
example of loss for all multipliers, a missed-force decomposition, a support floor, or a shifted-obstacle reading of the optimal multiplier.

**Verdicts (replacing Sec. 3 / Addendum E where different).**
- K1 (feasible-pair certificate) and K3 (minimisation of the surrogate over the multipliers) **are anticipated by Repin 2000/2007** (continuous, functional form); the
  paper now attributes them (Sec. 2, Sec. 3). The surrogate-to-majorant equivalence with constant $\frac43$ (K2) was not found in Repin.
- A1, A2 (certificate level), A3, A4, A5: **not found** in Repin 2000/2007 (and in no other text read). A1 is best described as the missing quantitative step for
  Repin-type minimised majorants: their efficiency relative to the primal error.
- The pre-registered rule (A1 together with A2 or A3) remains formally satisfied; the audit of the supplied sources is now complete except for the journal
  versions of BGK/HSW/Burkovska/Ashby-Pryer and unsupplied literature (Chen-Nochetto; Repin's later majorant papers and book chapters 8-9).
- **Remaining question before a go/no-go decision** (the review's point): whether the efficiency of minimised Repin-type majorants is a known or routine
  consequence for linear problems and carries over trivially; this is not answered by the texts read.

**Review points B–E applied to the manuscript:** three distinct conditions stated explicitly with the unknown-gap caveat (B); the $\kappa(K)\sim h^{-2}$ statement qualified for quasi-uniform FE (C);
the restricted shifted problem need not be feasible, certificate valid via $\hat u$ (D); the half rate is a limitation of the quadratic-root feasible-pair family, not an impossibility
theorem (E; supporting linear-bound sketch marked as unproved).
