# Proof audit guide (Gate S2 of RESEARCH_RECORD.md), prepared 23 Nov 2026

Purpose: let a second reader re-derive every proved statement independently. Proofs are in `certified-correction-contact-rom/paper/sections/02_setting.tex`
and `03_analysis.tex` (numbers as in the 23 Nov build). A check marked "tested" means the statement was verified numerically on random instances
(`experiments/e3.py`, 3 seeds x 1000 instances, 0 violations) and in unit tests (`tests/test_theory.py`, `tests/test_certificate.py`);
a numerical test does **not** replace the re-derivation.

**Common assumptions.** $K\succ0$ ($n\times n$), $B$ ($n_c\times n$) of full row rank, $X\succ0$ with $\alpha_XX\preceq K\preceq\gamma_XX$, $s^2=\gamma_X/\alpha_X$;
$(u,\lambda)$ the unique solution of $Ku-B^T\lambda=f$, $g=Bu-c\ge0$, $\lambda\ge0$, $\lambda^Tg=0$; $\hat u$ feasible ($\hat g=B\hat u-c\ge0$), $e=u-\hat u$; $\ell\ge0$ free;
$\bar\rho(\ell)=\|f+B^T\ell-K\hat u\|_{X^{-1}}/\sqrt{\alpha_X}$, $\eta(\ell)=\ell^T\hat g$, $\Delta^\star=\frac12(\bar\rho+\sqrt{\bar\rho^2+4\eta})$, $\Phi=\bar\rho^2+\eta$, $\ell^\star=\arg\min_{\ell\ge0}\Phi$.

| Statement | Re-derive | Assumptions actually used | Most likely hiding place of an error | Tested by |
|---|---|---|---|---|
| Prop 2.1 (certificate; established, formerly Thm 2.1) | $Ke=r+B^T(\lambda-\ell)$, $\|e\|_K^2=e^Tr+(g-\hat g)^T(\lambda-\ell)\le\|e\|_K\bar\rho+\eta$, then the quadratic | $\lambda^Tg=0$, $\ell,\lambda,\hat g,g\ge0$; $\|r\|_{K^{-1}}\le\bar\rho$ from $K\succeq\alpha_XX$ | direction of the $X^{-1}$ vs $K^{-1}$ inequality | E3 "Thm 3.1 lower" |
| Lem 2.2 ($\Phi\le\Delta^{\star2}\le\frac43\Phi$) | $\Delta^2=\bar\rho\Delta+\eta\ge\bar\rho^2+\eta$; maximise $\rho+\sqrt{4P-3\rho^2}$ | $\bar\rho,\eta\ge0$ | the maximiser lies in $[0,\sqrt P]$ | unit test; E3 "Lem 2.2 *" |
| Prop 2.3 (gap, $X=K$) | $J(\hat u)-D(\ell)=\frac12\bar\rho^2+\eta$; $J(\hat u)-J(u)=\frac12\|e\|^2+\lambda^T\hat g$; $\Delta^\star\le\sqrt{2G}$ with equality iff $\eta=0$ | $Ku-f=B^T\lambda$, $\lambda^Tg=0$ | sign of the dual function $D$ | E3 "Prop 2.3 *" |
| Thm 3.1 (efficiency) | $\Phi(\ell^\star)\le\Phi(\lambda)$; at $\ell=\lambda$ the residual is $Ke$; $\|Ke\|_{X^{-1}}^2\le\gamma_X\|e\|_K^2$; $\lambda^T\hat g=-\lambda^TBe\le m(\mathcal A_+)\|e\|_K$ | $\lambda\ge0$ admissible; $B^T$ injective for uniqueness of $\ell^\star$ | $\Phi(\lambda)$ uses $\eta(\lambda)=\lambda^T\hat g$ (not $\lambda^Tg$) | E3 "Thm 3.1 *" |
| Rem 3.2 (inexact S1, no $2/\sqrt3$ if $\eta(\ell^\star)=0$) | add $\delta$ in Lemma 2.2; $\Delta^\star=\bar\rho\le\Phi^{1/2}$ when $\eta=0$ | — | the second claim concerns $\eta(\ell^\star)=0$, not $\lambda^T\hat g=0$ | unit test; E3 "Rem 3.2 *" |
| Cor 3.3 (consistency) | divide Thm 3.1 by $\|e\|_K$ with $\lambda^T\hat g=0$ | — | uniformity requires a bound on $s$ (stated) | E3 "Cor 3.3" |
| Prop 3.5 (S1 = shifted contact problem, $X=K$) | $\nabla\Phi=2(D\ell+Bu_f-c-\frac12\hat g)$ using $B\hat u=c+\hat g$; KKT of the strictly convex $\Phi$; residual $=K(u'-\hat u)$; feasibility of $\hat u$ and $u'$ | $D\succ0$ (full row rank); uniqueness of the shifted contact problem | the factor $\frac12$ (from $2\cdot$ gradient of the quadratic part vs the linear term $\hat g$) | E3 "Prop 3.5 *", engine solver comparison |
| Cor 3.6 (exactness; now with the converse $\ell^\star=\lambda\Rightarrow0\le\hat g\le2g$) | $(u,\lambda)$ satisfies the shifted KKT iff $0\le\hat g\le2g$ (incl. $\hat g_i=0$ where $g_i=0$); uniqueness; then $\bar\rho=\|e\|_K$, $\eta=0$ | $X=K$ exactly (not $K(\bar\mu)$) | rows with $g_i=0$ and $\lambda_i=0$ (weakly active) also need $\hat g_i=0$ | E3 "Cor 3.6 *", E1 |
| Prop 4.1 (half rate example) | $\rho=|\ell-1-\varepsilon|$, $\eta=\ell\varepsilon$; $\min_\ell\Delta^\star=\sqrt{\varepsilon(1+\varepsilon)}$ at $\ell=1+\varepsilon$ | $N=2$, $n_c=1$ example | the case split $\ell\lessgtr1+\varepsilon$ in the proof | unit test (grid), numerical scan |
| Thm 4.2 (missed rows) | on $\mathcal A_+$: $g_i=0\Rightarrow\hat g_i=-(Be)_i$; only $\mathcal M$ contributes; Cauchy–Schwarz in the $K^{-1}/K$ pairing | $\lambda^Tg=0$ | $\mathcal M$ defined with $\hat g_i>0$ (not $\tilde g_i>0$): consistent with Cor 4.2 for snapped corrections | E3 "Thm 3.7 *" |
| Cor 4.3 (localised form, rate $(1+a)/2$) | Hölder on the finite sum; insert in Thm 3.1 | $a,C_\lambda,C_g$ assumptions | upper rate only; no matching lower bound claimed | E3 "Cor 3.8" |
| Thm 4.4 (restricted support) | upper: $\Phi(\ell^\star_S)\le\Phi(\lambda_S)$, residual $Ke-B^T\lambda_{S^c}$, $\|\cdot\|_{X^{-1}}\le\sqrt{\gamma_X}\|\cdot\|_{K^{-1}}$, triangle inequality; lower: $\sqrt{\alpha_X}\Delta\ge\|B^T(\lambda-\ell)\|_{X^{-1}}-\|Ke\|_{X^{-1}}\ge\sigma_S-\sqrt{\gamma_X}\|e\|_K$; $\sigma_S>0$ iff $\lambda_{S^c}\neq0$ | $B^T$ full column rank | $\Delta^\star\ge\bar\rho$ is used in the lower bound; $\sigma_S$ is a minimum over $v\in\mathbb R^{|S|}$ without sign constraint | E3 "Thm 3.9 *", E2 |
| Remark after Cor 3.6 (restricted S1 = shifted problem with constraints in $S$ only; $u'_S\ne u$) | KKT of $\Phi$ restricted to $S$; $u'_S=u$ would give $Ku-f\in\mathrm{range}\,B_S^T$ | $B^T$ injective | the claim is only for $u'_S\ne u$, not a quantitative bound | E2 (floor attained) |
| Props 6.1, 6.3, Cors 6.2, 6.4 (snapping) | $BB^+=I$ gives $\hat g_i=0$ on $\hat{\mathcal A}$ and $\tilde g^+$ elsewhere; $u_s=u_{R0}-B^+p$; $\beta=\|K^{1/2}B^+\|_2$ | — | the energy-norm of $B^+p$ vs $\beta\|p\|_2$ | unit tests |

**Not proved in the paper (must not be cited as results):** the linear bound $\|e\|\le\bar\rho+\|\hat g_J\|_{D_{JJ}^{-1}}$ for $J\supseteq$ contact sets of $u,u'$
(derived only as a sketch, `CLAIM_SHEET_AUDIT_RESULTS.md` Addendum C; marked `\verify` in the text); the rate claim $(1+a)/2$ is an upper rate only.

**Questions for the second reader.**
1. Is any use of $\lambda^T\hat g$ vs $\lambda^Tg$ mixed up in Thm 3.1, Cor 3.5, Thm 3.7?
2. Are the conditions of Cor 3.5 exactly $0\le\hat g\le2g$ (including $\hat g_i=0$ on the whole contact set), or is an extra condition missing?
3. In Thm 3.9, can $\sigma_S=0$ occur with $\lambda_{S^c}\neq0$ if $B$ is rank-deficient? (The paper assumes full row rank.)
4. Does anything in Secs. 2–3 secretly use the contact/ROM structure (selection matrix $B$, M-matrix $K$)? (None should; E3 uses dense random $B$.)
5. Is the attribution in Secs. 2–3 fair to Repin 2000/2007, Braess 2005, Krause–Veeser–Walloth 2015, Bartels et al. 2025, Repin–Valdman 2018?

**Numbering.** The table uses the numbering of the restructured paper (23 Nov 2026): Sections 3-4 are in `03_analysis.tex`, Section 6 in `06_application.tex`; the E3 labels in the generated table are cross-references. Statement added after the table was written: Remark 3.x (`rem:gap-comparison`: for X = K the argmin of the gap is the exact multiplier, and (||e||^2 + 2 lam.g)^(1/2) is compared with Thm 3.1); the second reader should re-derive it as well.

**Update 23 Nov 2026.** Numbers now: Rem 3.4 (gap comparison), Prop 3.5 (shifted problem), Cor 3.6 (exactness); Props 4.1, Thm 4.2, Cor 4.3, Thm 4.4; Props 6.1, 6.3 / Cors 6.2, 6.4. Questions 2 and 3 above refer to Cor 3.6 and Thm 4.4. The independent AI audit of 23 Nov found one false inequality (Cor 4.3, fixed); a human reader is still recommended.
