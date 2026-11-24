# Research record: efficiency and limitations of optimised-multiplier error certificates

Current reference for the present line of work (created 24 Nov 2026 from `archive/SHORT_PAPER_SCOPE.md`, `PROOF_AUDIT_GUIDE.md`, the manuscript sources and the saved results).
It covers the current scope only. Closed directions are listed in Sec. 1 with pointers and are not summarised. Statements about the literature mean "found in the texts read".

## 0. Snapshot

**Question.** For a feasible approximation of a discrete frictionless contact problem, how sharp is the minimum-residual feasible-pair error certificate (multiplier S1), and when does it fail?

**Message.** With $X=K$ the S1 multiplier is the solution of a contact problem with obstacle $c+\hat g/2$; it equals the exact multiplier iff $0\le\hat g\le2g$, and the certificate then equals the error. Otherwise it can degrade to the square-root rate (a missed primal contact row), and a multiplier restricted to a support that omits a strictly active row has a floor that does not decrease with the error (a missing dual support row).

**Is / is not.** A short numerical-analysis note on an established certificate family. Not a new certificate, multiplier, reduced-order method or correction method, and no claim that certification is cheaper than a full-order solve.

**Manuscript.** `certified-correction-contact-rom/paper/main.tex`; title *Efficiency and limitations of optimised-multiplier error certificates for discrete contact problems*; 16 pages; no venue chosen; author list not yet supplied.

| Gate | Status (24 Nov 2026) | Qualification |
|---|---|---|
| S1 Literature | Closed by author decision with accepted residual originality risk; **not verified** | Repin 2009 (ENUMATH) unread. A PDF of Chen-Nochetto (2000) is now in `literatures/` and has not been read. Six sources read only as preprints. The kill criterion (an earlier source stating the efficiency bound together with the exactness condition or the half-rate example) was not tested against the unread papers. |
| S2 Proof audit | Passed independent **AI** review after one fix | Two AI audits; no human reader yet. |
| S3 Evidence | Passed as reported (E1-E4) | Oracle-controlled; four protocol deviations disclosed (Sec. 4). |
| S4 Decision | **Pending (author)** | Requires (i) distinctness from earlier work and (ii) significance; see Sec. 6. |

## 1. How the scope changed

| Stage | Line of work | Outcome | Evidence pointer |
|---|---|---|---|
| Initial proposition | Certified post-solve correction of Galerkin contact ROMs, as a method paper | Closed: corrections dominated by enriched Galerkin; for constant K it reduces to static condensation | `FINAL_RESEARCH_PLAN.md` (decision log D1-D14), `CONTACT_RESPONSE_PLAN.md` |
| Selective enrichment, compression | Cheaper enrichment, contact-response bases | Closed: gate failed, displacement POD control matches | same files; `results/selective_gate`, `results/compression_stage1` |
| Current | Efficiency and failure mechanisms of the optimised-multiplier certificate | Active | this file |

The post-solve corrections survive only as an application (manuscript Sec. 6): examples of inconsistent and consistent feasible approximations.

## 2. Claims (current theorem numbers)

Setting: $K\succ0$, $B$ of full row rank, $X$ with $\alpha_XX\preceq K\preceq\gamma_XX$, $s^2=\gamma_X/\alpha_X$; $\hat u$ feasible, $\hat g=B\hat u-c\ge0$, $e=u-\hat u$; certificate $\Delta^\star(\ell)=\frac12(\bar\rho+\sqrt{\bar\rho^2+4\ell^T\hat g})$; S1 $=\arg\min_{\ell\ge0}\bar\rho^2+\ell^T\hat g$.

| # | Statement | Where | Standing | Closest prior work (what it lacks) |
|---|---|---|---|---|
| Known | Certificate $\|e\|_K\le\Delta^\star(\ell)$; $\Phi\le\Delta^{\star2}\le\frac43\Phi$; gap and energy identities | Prop. 2.1, Lem. 2.2, Prop. 2.3 | established, proofs included | Repin 2000/2007, Braess 2005, Krause-Veeser-Walloth 2015, Zhang et al., Bartels-Gudi-Kaltenbach 2025, Repin-Valdman 2018 |
| C1 | $\Delta^\star(\ell^\star)\le\frac2{\sqrt3}(s^2\|e\|_K^2+\lambda^T\hat g)^{1/2}$; consistency gives eff $\le\frac2{\sqrt3}s$ | Thm 3.1, Rem. 3.2, Cor. 3.3 | proved, tested; **modest** for $X=K$ (follows from the gap identity at the oracle multiplier, Rem. 3.4) | Repin: no efficiency bound; Haasdonk-Salomon-Wohlmuth: fixed multiplier |
| C2 | $X=K$: S1 solves the contact problem with obstacle $c+\hat g/2$; $\ell^\star=\lambda\iff0\le\hat g\le2g$; then $\Delta^\star=\|e\|_K$ | Prop. 3.5, Cor. 3.6 | proved, tested; the converse from certificate equality to multiplier recovery is **not** claimed | Repin-Valdman, BGK: contact term vanishes for covering contact sets (identity level); no effectivity statement. The reformulation itself is elementary |
| C3 | Example: $\min_{\ell\ge0}\Delta^\star=\sqrt{\varepsilon(1+\varepsilon)}$ while $\|e\|_K=\varepsilon$ | Prop. 4.1 | proved, tested; holds **within the certificate family only** | HSW Rem. 4.5 notes the square root; no example or optimum |
| C4 | $\lambda^T\hat g=-\lambda_M^TB e\le m(M)\|e\|_K$; localised bound, upper rate $(1+a)/2$ | Thm 4.2, Cor. 4.3 | proved, tested; rate is an upper rate, exponent not measured | Braess; Weiss-Wohlmuth (free-boundary localisation) |
| C5 | Restricted support $S$: upper bound, floor $\sigma_S$ when $\mathcal A_+\not\subseteq S$ | Thm 4.4 | proved, tested; fixed problem and support; $\sigma_S$ uses the exact multiplier | HSW (4.15) (dual error in the lower bound) |
| App | Snap-to-contact restores consistency; accuracy cost; gap rule | Props 6.1, 6.3, Cors 6.2, 6.4 | proved, tested; application only | none found |

Not claimed as a result: a linear-in-error bound using contact-set information (sketch only; stated as a limitation).

## 3. Mathematical map

| Statement | Source file | Assumptions used | Tested by | Audit remarks |
|---|---|---|---|---|
| Prop. 2.1 | `02_setting.tex` | feasibility; $\lambda^Tg=0$ | E3 | correct |
| Lem. 2.2 | `02_setting.tex` | $P=0$ case trivial | E3 (S1 and two random multipliers) | correct |
| Prop. 2.3 | `02_setting.tex` | $X=K$ | E3 | restrictions to $X=K$ added after audit 1 |
| Thm 3.1, Rem. 3.2, Cor. 3.3 | `03_analysis.tex` Sec. 3 | $\eta(\lambda)=\lambda^T\hat g$ (not $\lambda^Tg$); $\eta(\ell^\star)=0$ vs $\lambda^T\hat g=0$ distinguished | E3 | correct |
| Rem. 3.4 | `03_analysis.tex` | $X=K$; gap bound is at the oracle multiplier, not at S1 | E3 | wording fixed after audit 1 |
| Prop. 3.5, Cor. 3.6 | `03_analysis.tex` | $X=K$; $B^T$ injective; weakly active rows $g_i=\lambda_i=0$ require $\hat g_i=0$ | E1, E3 | equivalence proved after review; correct |
| Prop. 4.1 | `03_analysis.tex` Sec. 4 | example $N=2,n_c=1$ | numerics (`e_halfrate`) | case split verified |
| Thm 4.2 | `03_analysis.tex` | missed set $M=\{\lambda_i>0,\hat g_i>0\}$; $m(M)\le m(\mathcal A_+)$ need not hold | E1, E3 | loose sentence fixed |
| Cor. 4.3 | `03_analysis.tex` | Hölder (2,2) and (1,inf) as separate bounds; empty-set convention | E3 | **false inequality found and fixed** (audit 1) |
| Thm 4.4 | `03_analysis.tex` | $B^T$ injective; $\sigma_S$ without sign constraint | E2, E3 | correct |
| Sec. 6 results | `06_application.tex` | $BB^+=I$ | unit tests | consistent |
| Affine stiffness (Sec. 2.2) | `02_setting.tex` | $\theta_q(\bar\mu)>0$ and $\theta_q(\mu)>0$ for nonzero $K_q$, else a separate coercivity bound | none | assumption gap fixed after audit 2 |

## 4. Evidence

Pre-registered criteria were fixed before the runs (archived in `archive/SHORT_PAPER_SCOPE.md`, Sec. 4). All tables and figures are generated from saved results.

| ID | Experiment | Criterion (fixed beforehand) | Result |
|---|---|---|---|
| E1 | Exactness on finite element queries (membrane 576 unknowns, block 1452; $X=K$; 3 seeds; 3000 and 1200 queries); corrections R0, R0s (gap rule), R0s (multiplier rule) | where $0\le\hat g\le2g$: $|\mathrm{eff}-1|\le10^{-6}$; elsewhere $1\le\mathrm{eff}\le\frac2{\sqrt3}(1+\sqrt{m(M)/\|e\|})$ | max $|\mathrm{eff}-1|$ about $3\cdot10^{-14}$; share satisfying the condition: membrane 0 / 40 / 35 %, block 8 / 45 / 71 % (R0 / R0s gap / R0s multiplier); elsewhere median eff 1.01-1.50, max 4.89; no bound violation |
| E2 | Support floor on a controlled lift-off sequence (supports: all rows but $i^\ast$; $\mathcal A_+\setminus\{i^\ast\}$) | smallest-amplitude certificate $\ge0.95\,\sigma_S/\sqrt{\alpha_X}$ and $\ge100\times$ full S1 | equals $\sigma_S$ to 3 digits; ratio to full S1 at least 53,449 (block) and 65,044 (membrane); full S1 has slope about 1 |
| E2 diagnostic | Multipliers of the two supports | none (diagnostic) | restricted multiplier not zero outside $\mathcal A_+$ (up to about 12 % membrane, 40 % block of its largest entry); the two supports' multipliers differ by up to about 3 % / 8 %; certificates differ by at most about 1 % / 3 % (0.4 % for $\varepsilon\le10^{-3}$) |
| E3 | Random instances (1000 per seed, 3 seeds; sizes $(n,n_c)\in\{(8,3),(15,5),(30,8),(50,12)\}$; five kinds of $\hat u$) | zero violations beyond $10^{-9}$ relative | 0 violations of all tested statements; ratios of the two sides reported per statement (appendix table) |
| Half-rate | Prop. 4.1 example with the certificate code | none (illustration) | minimum matches $\sqrt{\varepsilon(1+\varepsilon)}$ to the minimiser's resolution (max relative deviation $4\cdot10^{-5}$); slope 0.49999; S1 multiplier $=1+\varepsilon/2$ with a certificate indistinguishable from the minimum at plot resolution |

**Protocol deviations after the first E3/E2 runs (disclosed in the manuscript, Sec. 5.4).**

| # | Change | Reason |
|---|---|---|
| 1 | Energy identity counted in the stable form $-e^T(Ku-f)+\frac12\|e\|^2$; direct difference kept as a diagnostic | cancellation produced $1.3\cdot10^{-9}$, $2.6\cdot10^{-9}$ against tolerance $10^{-9}$ |
| 2 | Reference solutions polished by an equality-constrained KKT solve | solver tolerance, not the statements, caused the discrepancy |
| 3 | Rounding allowance $\sim16\,n\,\varepsilon_{\rm mach}$ on the gap identity | discrepancies $1.4\cdot10^{-9}$, $1.2\cdot10^{-9}$ after Lem. 2.2 / Rem. 3.2 checks were added; observed at most 2.4 % of the allowance |
| 4 | M-matrix check removed in E2 | the block stiffness is not an M-matrix and the statement does not need it |

Limits of the evidence: two constant-stiffness benchmarks; random instances test the algebra, not the contact structure; queries share parameters across basis sizes and seeds (not independent observations); E2 uses the exact active set and exact multipliers (an illustration, not an online support-selection method); all computations in double precision; the tests are consistency evidence, not proofs.

**Saved results:** `results/e1_exactness/`, `results/e2_support_floor/` (including `multiplier_check_*.json`), `results/e3_random/`, `results/e_halfrate/`; reused earlier results: `results/gate0/`, `results/liftoff/`, `results/theory/`.

## 5. Literature

| Source | Cited for | Version read | Note |
|---|---|---|---|
| Repin 2000, 2007 | functional majorants, closed-form multiplier minimisation, no efficiency bound | original journal versions, full text | read in full |
| Zhang-Bader-Veroy (CR Acad. Sci. 2016); Zhang dissertation (RWTH 2016) | certificate, surrogate, $\Phi\le\Delta^2\le\frac43\Phi$ | as recorded in `CLAIM_SHEET_AUDIT_RESULTS.md` | dissertation cited generally; Lemma 2.2 carries no pinpoint (author decision) |
| Braess 2005; Krause-Veeser-Walloth 2015; Veeser 2001; Weiss-Wohlmuth 2010; Nochetto-Siebert-Veeser 2003; Benaceur-Ern-Ehrlacher 2020 | finite element forms, efficiency with multiplier error, localisation | as recorded in the audit | see `CLAIM_SHEET_AUDIT_RESULTS.md` |
| Repin-Valdman 2018; Bartels-Gudi-Kaltenbach 2025; Haasdonk-Salomon-Wohlmuth; Burkovska et al.; Ashby-Pryer 2024; Zhang-Bader-Veroy 2014 (arXiv 1410.2095) | identities, square-root observation, duality approach | **preprint / arXiv versions only** | theorem numbers refer to those versions; ZBV 2014: same certificate with the reduced-basis multiplier, sharpness shown numerically only, no efficiency theorem |
| Chen-Nochetto, Numer. Math. 84 (2000) 527-548 | residual-type estimators for obstacle problems | **unread**; PDF now in `literatures/` | bibliographic data verified on Crossref |
| Repin, ENUMATH 2009, pp. 755-762 | functional majorants for variational inequalities | **unread**; not obtained | bibliographic data verified on Crossref |

References in `paper/refs.bib`; only sources actually read are cited. The manuscript says "in the texts read" (Introduction) and that its literature statements rest on the texts read, with preprint versions for several sources (Sec. 4.1). The Conclusions no longer name the two unread papers (author instruction, 24 Nov 2026).

## 6. Verification history

| Date | Event | Found | Action |
|---|---|---|---|
| 23 Nov | Gate S3 | all criteria met; four protocol deviations | disclosed |
| 23 Nov | AI audit 1 (subagent re-derivation; 500 random falsification runs) | **false inequality in Cor. 4.3**; "never sharper" and the gap-certificate transfer valid only for $X=K$; gap-remark wording; Thm 4.2 sentence | all fixed |
| 23 Nov | External reviews (pasted) | abstract conflated certificate and multiplier; Table 3 ratio convention; support coincidence overstated; Cor. 3.6 equivalence; affine assumptions; contributions order | applied except where noted below |
| 23 Nov | E2 multiplier diagnostic | restricted multipliers are not equal and not zero outside $\mathcal A_+$ | text and figure legend corrected |
| 23 Nov | AI audit 2 (using `PROOF_READER_NOTE.md`) | no error in Thms/Props; needs $\theta_q(\mu)>0$ for $\alpha_X>0$ | fixed |
| 24 Nov | Review of the 16-page draft; ZBV 2014 preprint read | Delassus matrix name clash; duplicate table sentence; comparison with the duality approach | $H$ introduced; sentence and citation added |

Declined or kept: shortening the protocol-deviation paragraph (disclosure kept); restoring the Lemma 2.2 pinpoint citation (author removed it); the optional shifted-contact schematic (risk of a misleading drawing).

**S4 requirements.** (i) Distinctness: results not contained in, or immediately equivalent to, earlier analyses (gap identities, Repin-type majorants, finite element efficiency theory); a duplication check is necessary but not sufficient. (ii) Significance: new understanding of certification or a practically consequential limitation. The candidate argument is the contrast between a missed primal contact row (square-root loss) and a missing dual support row (a floor that does not decrease with the error), with the exactness condition for $X=K$. Whether this suffices for a journal article or only a note or technical report is the S4 judgement.

## 7. Open items

| Item | Owner | Note |
|---|---|---|
| Human mathematical reader | author | `PROOF_READER_NOTE.md` ready (placeholders for names); with `PROOF_AUDIT_GUIDE.md` |
| Read Chen-Nochetto (PDF now available); obtain Repin 2009 | author / assistant | would allow testing the S1 kill criterion |
| Author list and affiliations | author | title page placeholder |
| S4 decision (submit / technical report / stop) | author | after the reader reply |
| Journal versions of the preprint-only sources | author | would allow citing theorem numbers of the published versions |

## 8. File map and reproduction

| Location | Content |
|---|---|
| `certified-correction-contact-rom/paper/` | manuscript: `main.tex`, `sections/01_introduction.tex` ... `08_appendix.tex` (no `04`), `tables/`, `figures/`, `refs.bib` |
| `certified-correction-contact-rom/certcorrect/`, `tests/` | package (engine wrappers over `fea_engine` and `rom_engine`) and 93 tests |
| `certified-correction-contact-rom/experiments/` | current: `e1.py`, `e2.py`, `e2_mult.py`, `e3.py`, `halfrate.py`, `tables.py`, `figures.py`; older closed-line scripts (x1-x8, selective, compression, scaling) kept for the documented negative results |
| `certified-correction-contact-rom/results/` | saved results (see Sec. 4) |
| `PROOF_AUDIT_GUIDE.md`, `PROOF_READER_NOTE.md` | proof audit guide and cover note for a reader |
| `FINAL_RESEARCH_PLAN.md`, `CONTACT_RESPONSE_PLAN.md`, `CLAIM_SHEET*.md`, `ANALYSIS_T1_T3.md`, `THEOREM_certificate_efficiency.md`, `LITERATURE_REVIEW_week6.md`, `MATH_FORMULATION_v6c.md` | earlier plans, claim sheets and audits (source material) |
| `Guidlines/` | working-style, scripting, audit and reporting guidelines |
| `literatures/` | PDFs of the sources |
| `../certificate-efficiency/` (in `proposed-research/`) | self-contained copy of everything relevant to the manuscript (manuscript, current scripts, results, notes, literature); refreshed with `sync_from_repo.sh`; the originals listed here stay authoritative |
| `archive/` | superseded plans and notes, including `SHORT_PAPER_SCOPE.md` (the previous scope file with the pre-registered criteria and the dated status log) |

**Reproduction** (from `certified-correction-contact-rom/`, project `.venv`; seeds 0, 1, 2): see the README section "Reproducing the short paper". In short: `e1.py`, `e2.py`, `e2_mult.py` for each problem and seed; `e3.py --seed s --n-instances 1000`; `halfrate.py`; then `tables.py`, `figures.py`, and `latexmk -pdf -outdir=build main.tex` in `paper/`.
