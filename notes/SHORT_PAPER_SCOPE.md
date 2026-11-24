# Scope of the short analysis paper (23 Nov 2026)

Status: **scoping only; no manuscript commitment.** Basis: CLAIM_SHEET.md, CLAIM_SHEET_AUDIT_RESULTS.md (Addenda A–F),
CONTACT_RESPONSE_PLAN.md (status log), the draft in `certified-correction-contact-rom/paper/` (Secs. 1–4), and the saved
results in `certified-correction-contact-rom/results/`. Statements about the literature mean "not found in the texts read".

## 0. Current status (updated 23 Nov 2026)

Sections 1-8 below are the plan and protocol as fixed before the work; they are kept unchanged so that the acceptance criteria can be told apart from the
outcomes, except that theorem numbers in the claims table (Sec. 2) now follow the compiled manuscript. Outcomes are in the status log at the end of this file.

| Gate | Status | Qualification |
|---|---|---|
| S1 Literature | **Closed with accepted residual originality risk; not verified.** | Chen-Nochetto (2000) and Repin (2009) not obtained or read; four sources read only as preprints/arXiv. The kill criterion was not tested against the two unread papers. The paper states this in Sec. 7. |
| S2 Proof audit | **Passed independent AI mathematical review; human verification recommended.** | One false inequality found and fixed (Cor. 4.3). Random falsification tests (500 instances) are not a formal proof check. |
| S3 Evidence | **Passed as reported** (E1-E4). | Oracle-controlled (E2 uses exact active set and exact multipliers; it illustrates the theory, it is not an online support-selection algorithm). Four protocol changes after the first runs are disclosed. E2 follow-up: restricted multipliers are not zero outside A+ and differ between the two supports; certificates differ by <= 1-3 %. |
| S4 Decision | **Pending (author).** | Two separate requirements, both to be met (see below). |

**S4 requirements.** (i) *Distinctness*: the paper establishes results not contained in, or immediately equivalent to, earlier analyses (primal-dual gap identities,
Repin-type functional majorants, finite element efficiency theory). A literal duplication check (the S1 kill criterion) is necessary but not sufficient.
(ii) *Significance*: the results give a meaningful new understanding of certification or a practically consequential limitation. The candidate argument is the
distinction between a missed *primal* contact row (cost: square-root loss, Prop. 4.1 and Thm 4.2) and a missing *dual* support row (cost: a floor that does not
decrease with the error, Thm 4.4), and the exactness condition of Cor. 3.6 for X = K. Whether this is enough for a journal article, or only for a note or technical report, is the S4 judgement.
Note on the efficiency bound (C1): for X = K it is a modest extension of the gap identity (Remark 3.4); it should not be presented as the main contribution.

**Current theorem numbers (manuscript of 23 Nov 2026, 18 pages).** Prop 2.1 certificate (established result, formerly Thm 2.1); Lem 2.2; Prop 2.3 gap; Thm 3.1 efficiency; Rem 3.2; Cor 3.3; Rem 3.4 gap comparison;
Prop 3.5 shifted contact problem; Cor 3.6 exactness (with the equivalence l* = lam iff 0 <= g^ <= 2g, X = K); Prop 4.1 square-root degradation; Thm 4.2 missed rows;
Cor 4.3 localized form; Thm 4.4 restricted support; Props 6.1, 6.3 and Cors 6.2, 6.4 snapping. In the plan below, "Prop. 3.4 / Cor. 3.5" of the earlier numbering are Prop. 3.5 / Cor. 3.6.
The statement l* = lam is distinct from Delta* = ||e||_K: the first (for X = K) implies the second, and the converse is not claimed.

## 1. What the paper is, and is not

**Message (one sentence).** For feasible approximations of a discrete frictionless contact problem (more generally: a quadratic
program with linear inequality constraints), the efficiency of the minimum-residual feasible-pair error certificate is governed by one
quantity, $\lambda^T\hat g$; with $X=K$ it is exact under $0\le\hat g\le2g$, it degrades to the square-root rate in the worst case when a
strictly active row is open, and restricting the multiplier support can make the certificate stall.

**Is:** a short numerical-analysis note on the efficiency and failure mechanisms of an established certificate family, with controlled
numerical illustrations on finite element contact problems.
**Is not:** a new certificate, a new multiplier, a new ROM or correction method, or a statement that certification is cheaper than a full-order
solve. Those directions were tested and closed (decisions D12–D14; Stage 1 STOP).

**Working title.** *Efficiency and limitations of optimised-multiplier error certificates for discrete contact problems.*
(Alternative: *When is a feasible-pair error certificate for contact problems efficient?*)

**Generality.** The proofs use only $K\succ0$, full-row-rank $B$, and complementarity; the contact/ROM setting is the motivating application, and
Section 5 below (random-instance verification) is there to support the general statement.

## 2. Claims

| # | Statement (paper reference) | Status | Closest prior work (what it lacks) | Keep? |
|---|---|---|---|---|
| C1 | $\|e\|_K\le\Delta^\star(\ell^\star)\le\frac{2}{\sqrt3}\big(s^2\|e\|_K^2+\lambda^T\hat g\big)^{1/2}$; inexact S1 allowance (Thm 3.1, Rem. 3.2) | proved, tested | Repin 2000/2007 (minimised functional majorant, no efficiency bound); HSW (fixed multiplier, $O(\|e\|^{1/2})$); BGK (energy identity) | **core** |
| C2 | $\lambda^T\hat g=0\Rightarrow\mathrm{eff}\le\frac{2}{\sqrt3}s$ (Cor. 3.3); $X=K$ and $0\le\hat g\le2g\Rightarrow\Delta^\star=\|e\|_K$ (Prop. 3.5, Cor. 3.6) | proved, tested | Repin–Valdman 2018, BGK, KVW, Weiss–Wohlmuth: contact term vanishes for approximate contact sets covering the exact ones (identity level); no effectivity statement | **core** |
| C3 | optimum over all multipliers is $\sqrt{\varepsilon(1+\varepsilon)}$ in an explicit example (Prop. 4.1) | proved, tested | HSW Rem. 4.5 and Zhang Prop. 3.3.5 note the square root; no example or optimum | **core** (worst case, certificate family only) |
| C4 | $\lambda^T\hat g=\sum_{i\in\mathcal M}\lambda_i\hat g_i\le m(\mathcal M)\min(\|e\|,\|\tilde e\|)$; localized form, upper rate $(1+a)/2$ (Thm 4.2, Cor. 4.3) | proved, tested | Braess Rem. 1, Weiss–Wohlmuth Thm 3.7 (localisation to the free boundary, FE) | supporting |
| C5 | restricted support: bound and floor (Thm 4.4); mechanism via the shifted problem with only the constraints in $S$ | proved, tested | HSW (4.15) (dual error in the lower bound) | supporting; **the most distinctive failure mechanism** |
| C6 | S1 is the contact problem with obstacle $c+\hat g/2$ (Prop. 3.5) | proved, tested vs the engine solver | none found in the texts read (not Repin's "perturbed problem"); QP/KKT reformulations and obstacle perturbations have extensive prior art, so only the use of the equivalence for S1 is claimed, not the reformulation itself | supporting |
| C7 | relation to the primal–dual gap, $\Delta^\star\le\sqrt{2G}$ (Prop. 2.3) | proved, tested | identities: BGK, Repin–Valdman | remark only |
| C8 | snapping restores consistency; accuracy cost; gap rule (Props 6.1, 6.3, Cor. 6.4) | proved, tested | none found | **demote** to an application subsection (examples of inconsistent / consistent approximations) |

**Cited, not claimed:** the certificate (Braess 2005; Krause–Veeser–Walloth; Repin 2007; Zhang–Bader–Veroy), the minimum-residual multiplier and
its closed-form minimisation (Repin 2000/2007; Zhang 2016), $\Phi\le\Delta^{\star2}\le\frac43\Phi$ (Zhang 2016), the energy and gap identities (Repin–Valdman 2018; BGK).

## 3. Proposed structure (target about 14–16 pages including figures; venue not presumed)

| § | Content | From | Work |
|---|---|---|---|
| 1 | Introduction: certificates exist; what is missing (efficiency relative to the primal error); contributions C1–C5; what is not claimed | rewrite of `01_introduction.tex` | rewrite |
| 2 | Setting, certificate, S1, relation to gap and to Repin-type majorants | `02_setting.tex` | light edit |
| 3 | Efficiency: C1, C2 (incl. shifted problem and exactness) | `03_analysis.tex` | light edit |
| 4 | Failure mechanisms: C3, C4, C5 | `03_analysis.tex` | reorganise |
| 5 | Numerical illustration: controlled sequence, FE benchmarks, random instances | results + 3 new small experiments | new |
| 6 | Application: corrections of ROM predictions as consistent/inconsistent approximations (C8); one paragraph on the negative comparisons (consistent producers certify at 100 %) | `04_corrections.tex` shortened | cut ~60 % |
| 7 | Discussion and limits (unknown gap; cost of S1; scope) | new | short |

**Cut from the paper (kept in the repository):** offline–online evaluation, X6 timing, G/selective/compression studies, Gate 1 cost claims.

## 4. Evidence plan

**Reuse (saved results; tables to be generated by scripts, no hand-typed numbers):**
- rate and effectivity of R0 vs R0s: `results/gate0/summary.json` (membrane, block, layered; seeds 0–2), e.g. effectivity R0 1.74–1.96 vs R0s 1.00–1.44 with the gap rule;
- controlled lift-off sequence: `results/liftoff/membrane_seed0.npz` (R0 rate 0.51; R0s effectivity 1.0000000 at the smallest amplitude, consistent with Cor. 3.5);
- missed-row quantities and bound checks: `results/theory/*.npz` (all bounds hold on every query; exponents $a$);
- effectivity versus mesh for $X=K$ vs $X=I$: `results/x2*/`; restricted support: `results/x4/`.

**New (small; acceptance criteria fixed now, before running):**

| ID | Experiment | Acceptance criterion |
|---|---|---|
| E1 | Exactness on FE queries (membrane, block; $X=K$): fraction of R0/R0s queries with $0\le\hat g\le2g$ and the effectivity there | where the condition holds, $|\Delta^\star/\|e\|_K-1|\le10^{-6}$; elsewhere $1\le\mathrm{eff}\le\frac{2}{\sqrt3}(1+\sqrt{m(\mathcal M)/\|e\|})$ |
| E2 | Support floor on the controlled sequence: S1 with $S$ omitting the strictly active row of largest force | certificate at the smallest amplitude $\ge0.95\,\sigma_S/\sqrt{\alpha_X}$ and $\ge100\times$ the full-S1 certificate |
| E3 | Random-instance verification (property test, 1000 random SPD $K$, full-row-rank $B$, exact LCP solutions, random feasible $\hat u$): Thm 3.1, Cor. 3.3, Thm 3.7, Thm 3.9, Prop. 3.4, Cor. 3.5 | zero violations beyond $10^{-9}$ relative; equalities (Prop. 3.4 residual identity, Cor. 3.5, the identity in Thm 3.7) hold to $10^{-9}$; for the inequalities the observed ratio left/right side is reported per statement (no tightness is claimed except where proved: Prop. 3.6 optimum) |
| E4 | Seeds: repeat E1–E2 on seeds 0–2 | same criteria on every seed |

## 5. Work packages, gates and kill criteria

| Gate | What | Blocking question | Kill criterion |
|---|---|---|---|
| **S1 Literature closure** | read the sources not yet read: Repin's book (chapters on nonlinear problems/obstacles), Chen–Nochetto (cited by Veeser and Braess), the journal versions of BGK, HSW, Burkovska et al., Ashby–Pryer; targeted search for the efficiency of Repin-type majorants | does any source state a bound of a minimised majorant by the primal error plus the exact complementarity, a contact-set condition for effectivity one, or an example of unavoidable square-root loss? | any source states C1 and (C2 or C3) in equivalent form → close as a technical report |
| **S2 Proof audit** | independent re-derivation of every proof by a second reader; remove or prove the sketched linear bound (Addendum C) | is any step wrong or missing assumptions? | an error that invalidates C1 or C2 |
| **S3 Evidence** | run E1–E4; generate tables and figures from saved files | do the acceptance criteria hold? | a failure not explained by a stated assumption |
| **S4 Decision** | go/no-go on writing; venue and article type chosen after S1–S3 (check the length limits and scope of candidate journals; not asserted here) | are C1–C5 more than short corollaries in the eyes of a numerical-analysis reader? | author's judgement; fallback below |

**Effort (rough, working days):** S1 2–3 (once the texts are in hand); S2 1–2; S3 2–3; writing 5–8; internal review 2–3; total about 3–4 weeks elapsed.

## 6. Risks

1. **Novelty is narrow.** C1–C5 are short deductions from K1–K3 and the energy identity. Mitigation: state the scope honestly; lead with C2/C3/C5 (the explicit conditions, the example, the floor); keep the language "quantitative form for feasible-pair certificates of discrete (reduced) problems".
2. **Equivalence with a known efficiency theory** not yet read (Repin's later work, Chen–Nochetto). Mitigation: gate S1.
3. **Condition of Cor. 3.5 involves the unknown exact gap**, so it is analytical, not checkable online; stated in the text.
4. **Evidence is small-scale** (2D/3D benchmarks of a few thousand unknowns; one to three seeds). Mitigation: E3 supports the general statement; no cost or speed claims are made.
5. **Preprint-only reads** (BGK, HSW, Burkovska, Ashby–Pryer): attribution may need numbering changes (`\verify` tags in the draft).

## 7. Fallback

If S1 or S2 kills the claims, or S4 judges the content insufficient: keep the repository as validated code (93 tests), the documented negative results (post-solve correction, selective and compressed enrichment, G), and this note, as a technical report; no manuscript.

## 8. Needed from the author

1. Go-ahead for S1–S3 (about 1.5 weeks of work before the S4 decision).
2. The remaining literature (list in Sec. 5, S1); the Repin book chapters are the priority.
3. A second reader for S2 (a colleague or a different tool-independent check of the proofs).
4. Any preference on article type and length, to be weighed at S4 (not before).

## Status: Gate S3 (numerical evidence), recorded 23 Nov 2026

Outcome: E1-E4 acceptance criteria met. Results in `certified-correction-contact-rom/results/{e1_exactness,e2_support_floor,e3_random}/`;
LaTeX tables generated by `experiments/tables.py` into `paper/tables/` (compile-tested standalone). Figures `paper/figures/fig_e1_effectivity` and `fig_e2_support_floor` (PDF+PNG) generated by `experiments/figures.py` from the saved .npz files.

- **E1 (FE exactness, X = K):** where 0 <= g^ <= 2g holds, |eff-1| <= 3e-14 (criterion 1e-6); elsewhere 1 <= eff <= (2/sqrt3)(1+sqrt(m(M)/||e||)) with no violations.
  Share of queries satisfying (C), membrane 0/40/35 % and block 8/45/71 % for R0 / R0s (gap rule) / R0s (multiplier rule).
- **E2 (support floor):** restricted-support certificate equals sigma_S to 3 digits and is >= 53,000x the full-S1 certificate; membrane and block, 3 seeds.
- **E3 (random SPD / full-row-rank instances, 3 seeds x 1000):** 0 violations of Lem 2.2, Rem 3.2, Thm 3.1, Cor 3.3, Thm 3.7, Cor 3.8, Thm 3.9, Prop 2.3, Prop 3.4, Cor 3.5.

**Deviations from the pre-registered protocol (to be disclosed in the paper; all made after seeing first results):**
1. Prop 2.3 energy identity is counted in the algebraically stable form -e.(Ku-f)+0.5||e||^2; the direct difference J(u^)-J(u) is reported only as a diagnostic with a rounding allowance (cancellation produced 1.3e-9 and 2.6e-9 > 1e-9 otherwise).
2. The reference solution of each random instance is polished by an equality-constrained KKT solve on its active set (solver tolerance, not the theory, caused the violations).
3. A rounding allowance 16 n eps (...) was added to the gap identity after violations of 1.4e-9 and 1.2e-9 appeared when the Lem 2.2 / Rem 3.2 checks were added; observed discrepancies are <= 2.4 % of the allowance.
4. E2: the M-matrix check was removed (the block stiffness is not an M-matrix; only g^ = 0 on A_+ is needed).
No tightness is claimed except Prop 3.6.

Still open: S1 (literature closure; needs Repin book ch. 8-9, Chen-Nochetto, journal versions of BGK / HSW / Burkovska / Ashby-Pryer), S2 (independent proof audit; see PROOF_AUDIT_GUIDE.md), then S4 go/no-go (author decision).

## Status: manuscript restructured, 23 Nov 2026
`certified-correction-contact-rom/paper/` now follows Sec. 3 of this note: 1 Introduction, 2 Setting, 3 Efficiency, 4 Failure mechanisms, 5 Numerical results (E1-E3),
6 Application (corrections, shortened), 7 Discussion and limitations; new title and abstract; online/pending sections removed; builds without undefined references.
Provisional until S1 (literature closure) and S2 (proof audit) are done; no venue chosen.

## Review follow-up, 23 Nov 2026
- External review (pasted by the author) checked against the repository: figure status inconsistency in CONTACT_RESPONSE_PLAN.md fixed; the review's point that for X = K the minimised primal-dual gap gives an efficiency bound from the energy identity is correct and is now Remark 3.x (`rem:gap-comparison`) in the paper: argmin of G is the exact multiplier (the full-order dual), the bound (||e||^2+2 lam.g)^(1/2) is neither implied by nor implies Thm 3.1, and the S1-specific content is the computable minimiser, general X (s > 1), and Cor 3.5 / Prop 4.1 / Thm 4.4, which do not follow from the gap identity. Consequence: Sec. 1 claim C1 should be described as a modest extension for X = K.
- S1 reading list additions (not yet read; bibliographic data from the review, unverified on Crossref): Repin, "A posteriori estimates for variational inequalities", Numerical Mathematics and Advanced Applications 2009, pp. 755-762; Chen-Nochetto, Numer. Math. 84 (2000) 527-548.
- Sections 3-4 are both in `paper/sections/03_analysis.tex`; there is no separate failure-mechanisms file.
- 23 Nov 2026: both added S1 references now verified on Crossref (not yet read, not cited in the paper): Chen and Nochetto, Numer. Math. 84 (2000) 527-548, doi 10.1007/s002110050009; Repin, "A Posteriori Estimates for Variational Inequalities", Numerical Mathematics and Advanced Applications 2009 (Springer, published 2010), pp. 755-762, doi 10.1007/978-3-642-11795-4_81. Both are paywalled; PDFs needed from the author for gate S1.

## Gate S2 (independent proof audit by a subagent), 23 Nov 2026
Performed by an independent model instance (not a human reader) that re-derived every proof from the manuscript sources without the author's tests. Result: all proofs correct except one false inequality;
fixed in the paper: (1) Cor 4.3, eq. (localized): the middle step ||lam_M||_2 ||g_M||_2 <= ||lam_M||_1 max g_i is false (lam=(1,0), g=(1,1)); now two separate bounds under a min; the rate (1+a)/2 was unaffected.
(2) Sec. 2: "never sharper" and "sqrt(2G) >= Delta*, so the half rate applies to gap certificates" now restricted to X = K (for X != K, sqrt(2G) can be below Delta*).
(3) Remark on the gap comparison: the gap bound is at the oracle multiplier, not at S1; S1 inherits a bound of the same form via Phi(l*) <= Phi(lam) and Phi <= Delta^2 <= 4/3 Phi.
(4) Thm 4.2 follow-up sentence: no longer claims to contain Cor 3.3(a); m(M) <= m(A+) need not hold. (5) The paper no longer says the exponent a is measured; C_g = max_i D_ii^(1/2) noted as automatic. (6) Typo "close to one"; "iff" for Cor 3.5 added.
Numerical falsification attempts (300 + 200 random instances, general SPD X): 0 violations. Not verified by the audit: literature attributions (theorem numbers in cited papers), the linear bound marked \verify, kappa(K) ~ h^-2.
S2 status: passed by an AI second reader after one fix; a human second reader is still advisable before submission.

## Gate S1 closed with stated risk, 23 Nov 2026 (author decision)
Chen-Nochetto (2000) and Repin (2009, ENUMATH) could not be obtained and were not read. S1 is closed with this risk stated in Sec. 7 (Limitations, "Literature"): the efficiency bound, the exactness condition or the half-rate example may exist in an equivalent form in unread work.
This is a closure by decision, not by evidence; the kill criterion of S1 (an equivalent statement of C1 and C2 or C3 in a source) has not been tested against these two papers.

## Proofreading report applied, 23 Nov 2026
External proofreading report (pasted by the author) checked against the manuscript. Applied: abstract rewritten (the multiplier, not the certificate, solves the shifted contact problem; floor qualified as "for a fixed problem ... as the error tends to zero"; square-root degradation "within this certificate family"); introduction literature sentence softened; "never sharper" restated for the same multiplier and X = K; Prop 4.1 titled and qualified as a property of the certificate family; Thm 4.4 remark that the lower bound is informative only for ||e|| < sigma_S/sqrt(gamma_X); Fig. 1 caption; Table 3 caption explains counts above 3000 (Lemma 2.2: S1 + two random multipliers per instance; Thm 4.4: two supports per instance; verified in e3.py); language edits in Secs. 3, 5, 6; "TO DECIDE" note removed from refs.bib.
Not applied: shortening the protocol-deviation paragraph in Sec. 5.4 (kept in full, since disclosure is the point); restructuring Lemma 2.2's proof (it already introduces P = rho^2 + eta); removing the \verify markers (three remain, deliberately, until journal versions are checked); author list (needs the author).

## Second review applied, 23 Nov 2026
Applied: Cor 3.5 now states and proves the equivalence l* = lam iff 0 <= g^ <= 2g (X = K; l* = lam implies lam.g^ = 0 hence Delta* = ||e||; the converse for the certificate is not claimed); affine-stiffness assumptions (theta_q(mu-bar) > 0 where K_q != 0, K(mu) positive definite; X = I constants); sigma_S flagged as a diagnostic using the exact multiplier, directly after Thm 4.4; Table 3: the Thm 4.4 lower-bound row is labelled with the inequality and the caption states that lower-bound ratios are lower bound / certificate (the table was correct: lhs/rhs with lhs the lower bound; checked in e3.py); coincidence of the two restricted supports (E2) now an empirical observation (sigma_S is the same for both, the restricted S1 minimisers need not coincide); caption of Fig. 2 notes the exact multipliers; queries are not independent observations (Sec. 5.1); contributions reordered (exactness first); "governed by" wording. Not applied: removal of \verify markers (author decision pending); figure overplotting (markers already small and transparent).
Not checked: the claim that the E2 restricted S1 multipliers are zero outside A+ (not tested; reported as observation only).

## Follow-up tasks, 23 Nov 2026
- \verify markers removed: replaced by plain statements of what was read (arXiv/preprint versions; the linear bound is a sketch, not claimed).
- E2 diagnostic (`experiments/e2_mult.py`, 3 seeds x 2 problems, results in results/e2_support_floor/multiplier_check_*.json): the restricted S1 multiplier is NOT zero outside A+ (up to ~12 % membrane, ~40 % block of its largest entry) and the two supports' multipliers differ on A+ minus i* by up to ~3 % / ~8 %; the two certificates differ by at most ~1 % / ~3 % over all amplitudes (<= 0.4 % for eps <= 1e-3). Paper text and Fig. 2 legend corrected accordingly ("nearly coincide"; earlier wording "coincide"/"same values" was too strong).
- README: section "Reproducing the short paper" with the command sequence.

## Figure and table suggestions applied, 23 Nov 2026
Added: Fig. 3 (`fig_halfrate`, Sec. 4.1): Prop. 4.1 example, generated by `experiments/halfrate.py` with the certificate code (results/e_halfrate/): minimum over multipliers matches sqrt(eps(1+eps)) to the numerical minimiser's resolution (max relative deviation 4e-5), log-log slope 0.49999, S1 multiplier = 1 + eps/2 (median of (l-1)/eps = 0.5) with a certificate indistinguishable from the minimum at plot resolution; Table "benchmarks" (Sec. 5.1) generated from the problem objects and config (N = 576 / 1452, n_c = 144 / 121, mesh, element, training/test sizes, basis sizes).
Not added: the shifted-contact schematic (optional; risk of a misleading drawing), moving Table 3 to an appendix (kept in the main text for now). The manuscript is now 18 pages.

## Independent reader report (AI), 23 Nov 2026
Second AI audit using PROOF_READER_NOTE.md: no error found in Thms 2.1-4.4; one required assumption fix, applied: affine stiffness needs theta_q(mu) > 0 for the ratio alpha_X = min_q theta_q(mu)/theta_q(mu-bar) to be positive (a zero coefficient gives alpha_X = 0 although K(mu) may be SPD; the earlier fix required only theta_q(mu-bar) > 0). Also applied: empty-set convention in Cor 4.3; P = 0 case in Lem 2.2; redundant necessity illustration after Cor 3.6 removed; sensitivity assertion in Sec. 4.1 reworded to "one may expect ... not proved"; Discussion "efficiency bound is governed by". Not applied: moving Table 3 to an appendix. Still outstanding: human mathematical reader; Chen-Nochetto (a public manuscript copy may be on CiteSeerX, per the report, unverified) and Repin 2009.

- 23 Nov 2026: Table 3 (E3) moved to Appendix A (sections/08_appendix.tex).
- 23 Nov 2026: free copy of Chen-Nochetto (2000) checked: none found (a second search again found only the publisher page and the author's abstract page; the CiteSeerX copy suggested in an AI report is not confirmed). S1 stays closed with stated risk; a library or interlibrary-loan copy is the remaining route.

- 24 Nov 2026 (author instruction): the Conclusions section no longer names the two unread sources (Chen-Nochetto 2000, Repin 2009) or says that equivalent results may exist in unexamined work; the run-in headings were removed. The S1 closure note above ("risk stated in Sec. 7") therefore no longer holds in that form. What remains in the paper: the introduction says "in the texts read", and Sec. 4.1 states that statements about the literature rest on the texts read (original papers of Repin 2000/2007; preprint or arXiv versions of the others; journal versions not checked).

## Review of 24 Nov 2026 (main(10).pdf), applied
- Read arXiv 1410.2095 (Zhang, Bader, Veroy, "A duality approach ...", preprint; read in the arXiv version only): its primal-dual bound (Prop. 4.3) is the same feasible-pair certificate with the reduced-basis multiplier (no optimised multiplier) and a strictly feasible slack-based approximation; sharpness ("mimics the convergence rate") is shown numerically on a 1D rope and a 2D membrane, with no efficiency theorem. It does not contradict the square-root example (restricted to the certificate family) and contains none of C1-C5. Added one comparison sentence to the Introduction and a @misc entry (zhang2014arxiv) flagged as a preprint.
- Delassus matrix renamed H (was D; the dual function is calligraphic D); duplicate Table 1 sentence removed; British spelling made consistent in the Introduction; "double-precision" sentence added to Sec. 5.1; Appendix A moved before the bibliography.
- Not applied: restoring the citation for Lemma 2.2 (the author removed it on 23 Nov; the opening sentence of Sec. 2.4 cites the dissertation generally); shortening Table 4's caption.
