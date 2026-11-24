# Analysis T1–T3: missed rows, over-snapping and restricted multipliers

Week 3 of FINAL_RESEARCH_PLAN.md (Sec. 3, "New theory"). Builds on THEOREM_certificate_efficiency.md (Theorem E,
Corollary E1, Propositions E2–E3), whose notation is used throughout. Written 23 Nov 2026. Numerical checks:
`certified-correction-contact-rom/experiments/check_theory.py` (Section 5).

Novelty is stated relative to the sources read for THEOREM_certificate_efficiency.md (Haasdonk–Salomon–Wohlmuth 2012,
Zhang–Bader–Veroy 2014/2016, Zhang 2016). The results below are elementary consequences of Theorem E; their value is
that they explain the Gate 0 observations and give design rules. The literature recheck of week 14 applies to them.

---

## 0. Setting and additional notation

Full-order solution $(u,\lambda)$: $Ku-B^T\lambda=f$, $g=Bu-c\ge0$, $\lambda\ge0$, $\lambda^Tg=0$; $K\succ0$, $B$ of full
row rank; $\alpha_XX\preceq K\preceq\gamma_XX$, $s^2:=\gamma_X/\alpha_X$ ($s=1$ for $X=K$).

- Lifted ROM prediction $\tilde u$, its error $\tilde e:=u-\tilde u$, its gap $\tilde g:=B\tilde u-c$ (any sign).
- Strictly active set $\mathcal A_+:=\{i:\lambda_i>0\}$; true contact set $\mathcal A:=\{i:g_i=0\}\supseteq\mathcal A_+$.
- Predicted active set $\hat{\mathcal A}$ and the snap correction (R0s; Proposition E3)
$$
d_i=\begin{cases}c_i-(B\tilde u)_i=-\tilde g_i,& i\in\hat{\mathcal A},\\ \max(0,-\tilde g_i),& i\notin\hat{\mathcal A},\end{cases}\qquad
\hat u=\tilde u+B^+d,\qquad \hat g:=B\hat u-c,\qquad e:=u-\hat u .
$$
  R0 is the case $\hat{\mathcal A}=\emptyset$. From $BB^+=I$: $\hat g_i=0$ on $\hat{\mathcal A}$, $\hat g_i=\tilde g_i^+:=\max(\tilde g_i,0)$ off $\hat{\mathcal A}$.
- For a row set $M$, $\lambda_M$ is $\lambda$ with the entries outside $M$ set to zero, and
$$
m(M):=\|B^T\lambda_M\|_{K^{-1}}\qquad(\text{contact intensity carried by the rows }M).
$$
  $m(\mathcal A_+)=\|B^T\lambda\|_{K^{-1}}=\|u-K^{-1}f\|_K$ is the quantity of (E2); $m(\emptyset)=0$.
- Two identities used repeatedly: for $i\in\mathcal A$ (so $g_i=0$),
$$
\tilde g_i=-(B\tilde e)_i,\qquad \hat g_i=-(Be)_i, \tag{0.1}
$$
  because $\tilde g=g-B\tilde e$ and $\hat g=g-Be$.

---

## 1. T1: certificate excess from missed rows

**Definition.** The *missed rows* of the correction are
$$
M:=\{i\in\mathcal A_+\setminus\hat{\mathcal A}:\ \tilde g_i>0\},
$$
the rows in contact with a positive force in the truth that the ROM predicts open and the correction leaves open.
For R0, $M=\{i\in\mathcal A_+:\tilde g_i>0\}$.

**Theorem T1.** For R0 and for R0s with any $\hat{\mathcal A}$,
$$
\lambda^T\hat g\;=\;\sum_{i\in M}\lambda_i\tilde g_i\;=\;-\lambda_M^TB\tilde e\;=\;-\lambda_M^TBe\;\le\;m(M)\,\min\big(\|e\|_K,\|\tilde e\|_K\big), \tag{T1.1}
$$
and the S1 certificate satisfies
$$
\|e\|_K\le\Delta^\star(\ell_{S1})\le\frac{2}{\sqrt3}\Big(s^2\|e\|_K^2+m(M)\min\big(\|e\|_K,\|\tilde e\|_K\big)\Big)^{1/2}. \tag{T1.2}
$$

*Proof.* $\lambda^T\hat g=\sum_{i\in\mathcal A_+}\lambda_i\hat g_i$. On $\hat{\mathcal A}$, $\hat g_i=0$; off $\hat{\mathcal A}$, $\hat g_i=\tilde g_i^+$, which is
nonzero only where $\tilde g_i>0$. Hence the sum runs over $M$ and equals $\sum_M\lambda_i\tilde g_i$. Since $M\subseteq\mathcal A_+\subseteq\mathcal A$,
(0.1) gives $\tilde g_i=-(B\tilde e)_i$ and, because $\hat g_i=\tilde g_i$ on $M$, also $\tilde g_i=-(Be)_i$. Therefore
$\lambda^T\hat g=-(B^T\lambda_M)^T\tilde e=-(B^T\lambda_M)^Te$, and Cauchy–Schwarz in the $K^{-1}$/$K$ pairing gives (T1.1).
(T1.2) is (E1) of Theorem E with (T1.1) inserted. $\square$

**Corollary T1 (two regimes).** With $\sqrt{a+b}\le\sqrt a+\sqrt b$,
$$
\mathrm{eff}:=\frac{\Delta^\star(\ell_{S1})}{\|e\|_K}\le\frac{2}{\sqrt3}\Big(s+\sqrt{m(M)/\|e\|_K}\Big). \tag{T1.3}
$$
The half-rate term exceeds the full-rate term only when
$$
\|e\|_K<\frac{m(M)}{s^2}=:e_\times . \tag{T1.4}
$$
For $\|e\|_K\ge e_\times$ the effectivity is at most $\frac{4}{\sqrt3}s$ ($\approx2.31$ for $X=K$), whatever $M$ is; the certificate
then follows the error at the full rate up to this factor. The half rate of Proposition E2 is an asymptotic statement
for $\|e\|_K\ll e_\times$.

*Sharpness.* In the example of Proposition E2, $M=\{1\}$, $m(M)=1$, $\|e\|_K=\varepsilon$: (T1.2) gives
$\Delta^\star\le\frac2{\sqrt3}(\varepsilon^2+\varepsilon)^{1/2}$ and Proposition E2 gives $\Delta^\star\ge\sqrt{\varepsilon/2}$, so (T1.2) is attained up to the
factor $2\sqrt2/\sqrt3\approx1.63$ as $\varepsilon\to0$.

**Corollary T1b (localized form and intermediate rates).** From the first equality in (T1.1),
$$
\lambda^T\hat g=\sum_{i\in M}\lambda_i\hat g_i\ \le\ \|\lambda_M\|_2\,\|\hat g_M\|_2\ \le\ \|\lambda_M\|_1\max_{i\in M}\hat g_i . \tag{T1.5}
$$
If, along a sequence of approximations, $\|\lambda_M\|_1\le C_\lambda\|e\|_K^{a}$ and $\max_M\hat g_i\le C_g\|e\|_K$ for some $a\in[0,1]$, then
$$
\Delta^\star(\ell_{S1})\le\frac{2}{\sqrt3}\Big(s\|e\|_K+(C_\lambda C_g)^{1/2}\|e\|_K^{(1+a)/2}\Big), \tag{T1.6}
$$
i.e. the certificate is bounded above at order $\|e\|_K^{(1+a)/2}$ (and at the full rate where the first term dominates).
$a=0$ (missed rows keep a fixed force) is the worst case of Proposition E2; $a=1$ is the full rate. *(Wording corrected
23 Nov 2026 after an external audit: this is an upper rate; a matching lower bound for S1 is not proved, so $(1+a)/2$
is consistent with the measured rates but is not shown to be the exact asymptotic rate.)*

*Proof.* Hölder's inequality on the finite sum, then (E1) with $\sqrt{x+y}\le\sqrt x+\sqrt y$. $\square$

**Remarks.**
1. *Interpolation.* $M=\emptyset$ is Corollary E1(b); $M=\mathcal A_+$ recovers Corollary E1(a), since $m(\mathcal A_+)=\|B^T\lambda\|_{K^{-1}}$.
   T1 replaces the total contact intensity by the intensity on the missed rows only.
2. *Gate 0, qualification 1 (corrected after the checks of Section 5).* The first explanation considered, that the
   errors lie in the pre-asymptotic regime $\|e\|_K\ge e_\times$ of (T1.4), is **not** supported: for R0 the median
   $m(M)/\|e\|_K$ is 2.7–16.5, and on the membrane no query satisfies $\|e\|_K\ge e_\times$. The energy form (T1.1) is valid but
   loose (median tightness 0.04–0.24 for R0), because it ignores that the missed rows are few and carry little force.
   The measured mechanism is that of Corollary T1b: $\|\lambda_M\|_1$ decreases with the error ($a\approx0.3$–$0.9$ for R0)
   while $\max_M\hat g_i$ scales roughly like $\|e\|_K$, so the excess grows like $\|e\|_K^{1.2\text{–}1.5}$ and the certificate rate
   lies between 1/2 and 1. That the missed rows sit at the edge of the contact zone, where the pressure is small, is
   the likely reason for $a>0$; this is a heuristic, not shown here.
3. *Consequence for a lift-off benchmark.* To show the half rate, the missed rows must keep a fixed force ($a\approx0$):
   contact that the ROM predicts open in the interior of the true contact zone. The planned lift-off benchmark should
   be designed for that (load centre outside the training patch, so that the true contact zone is not represented in
   the snapshots); its acceptance check is $a\approx0$ in the measurement of Section 5.
4. $M$ depends on the unknown $\lambda$; T1 is an analysis result, not an online quantity.

---

## 2. T2: accuracy cost of snapping

**Proposition T2 (exact form).** Let $p_i:=\tilde g_i^+$ for $i\in\hat{\mathcal A}$ and $p_i:=0$ otherwise. Then
$$
\hat u_{snap}=\hat u_{R0}-B^+p,\qquad e_{snap}=e_{R0}+B^+p,\qquad
\big|\,\|e_{snap}\|_K-\|e_{R0}\|_K\big|\le\|B^+p\|_K\le\beta\,\|p\|_2, \tag{T2.1}
$$
with $\beta:=\|K^{1/2}B^+\|_2=\lambda_{\max}\big((B^+)^TKB^+\big)^{1/2}$, a property of the mesh and the constraints only.

*Proof.* The two corrections differ only on $\hat{\mathcal A}$, where $d^{snap}_i-d^{R0}_i=-\tilde g_i-\max(0,-\tilde g_i)=-\tilde g_i^+$. Linearity of
$B^+$ gives the first two identities; the triangle inequality and the definition of $\beta$ give the bound. $\square$

**Corollary T2a (where the cost comes from).** Split $\hat{\mathcal A}$ into the truly closed rows $\hat{\mathcal A}\cap\mathcal A$ and the
over-snapped rows $O:=\hat{\mathcal A}\setminus\mathcal A$. Then
$$
p_i\le|(B\tilde e)_i|\ \ (i\in\hat{\mathcal A}\cap\mathcal A),\qquad p_i\le g_i+|(B\tilde e)_i|\ \ (i\in O), \tag{T2.2}
$$
so $\|e_{snap}\|_K\le\|e_{R0}\|_K+\beta\big(\|B\tilde e\|_{2,\hat{\mathcal A}}+\|g\|_{2,O}\big)$. The first term is of the order of the ROM error; the
second is of the order of the **true gap on the over-snapped rows** and does not vanish when the ROM error does.

*Proof.* $\tilde g=g-B\tilde e$; on $\mathcal A$, $g_i=0$. $\square$

This explains the Gate 0 observation that the multiplier rule (which selects rows by $\tilde\lambda_i>0$, with no control on
$\tilde g_i$) gave R0s errors of 17–234 %: the over-snapped rows are pulled onto the obstacle across their full true gap.

**Corollary T2b (gap rule).** For the gap rule $\hat{\mathcal A}_t=\{i:\tilde g_i\le t\}$ (here $t=\tau_g\cdot\mathrm{char\_gap}$), every $p_i\le t$, so
$$
\|e_{snap}\|_K\le\|e_{R0}\|_K+\beta\,t\,|\hat{\mathcal A}_t|^{1/2}. \tag{T2.3}
$$
The accuracy cost is bounded a priori by the threshold, whatever the true contact set is.

**Corollary T2c (T1 and T2 together, gap rule).** Rows with $\tilde g_i\le t$ are snapped, so the missed rows satisfy
$M\subseteq\{i\in\mathcal A_+:\tilde g_i>t\}=\{i\in\mathcal A_+:-(B\tilde e)_i>t\}$ by (0.1). Hence
$$
\|B\tilde e\|_\infty\le t\ \Longrightarrow\ M=\emptyset,\ \ \mathrm{eff}\le\frac{2}{\sqrt3}s,\ \ \|e_{snap}\|_K\le\|e_{R0}\|_K+\beta\,t\,|\hat{\mathcal A}_t|^{1/2}. \tag{T2.4}
$$
The threshold trades the two effects: a larger $t$ covers more of $\mathcal A_+$ (T1 excess down) at a larger
accuracy cost (T2 up). The natural scale is $t\approx\|B\tilde e\|_\infty$, the ROM error in the constraint space; it is not
known online, which is why $t$ is chosen by the certified share (X3).

**Remarks.**
1. $\beta$ depends on the mesh. For a node-selection $B$ with unit entries, $B^+=B^T$ and $(B^+)^TKB^+=BKB^T$ is
   the stiffness restricted to the contact unknowns, so $\beta^2\le\max_i\sum_j|K_{ij}|$ over contact rows. For the
   Poisson membrane this is $O(1)$ in $h$; for 3D linear elasticity on a uniform mesh, $O(h)$ (entries scale like $h^{d-2}$).
   With a fixed physical threshold $t$, the number of snapped rows grows like $h^{-(d-1)}$; (T2.3) is therefore not
   uniform in $h$. The energy-projection variant Bs removes the nodal character of the correction (weeks 5–6).
2. T2 is a statement about the error, not about the certificate; the certificate stays valid for every $\hat{\mathcal A}$ and
   reports the cost of over-snapping (with effectivity near 1, as observed).

---

## 3. T3: restricted support of the S1 multiplier

For $S\subseteq\{1,\dots,n_c\}$, let $\ell_S:=\arg\min\{\Phi(\ell):\ell\ge0,\ \ell_i=0\ (i\notin S)\}$ (S1-restricted; $S=\{1..n_c\}$ is S1).

**Theorem T3.** For every feasible $\hat u$ and every $S$:
$$
\Delta^\star(\ell_S)\le\frac{2}{\sqrt3}\Big(s^2\big(\|e\|_K+m(S^c)\big)^2+\lambda^T\hat g\Big)^{1/2}, \tag{T3.1}
$$
$$
\Delta^\star(\ell_S)\ \ge\ \frac{\sigma_S-\sqrt{\gamma_X}\,\|e\|_K}{\sqrt{\alpha_X}},\qquad
\sigma_S:=\min_{v\in\mathbb R^{|S|}}\big\|B^T\lambda_{S^c}-B_S^Tv\big\|_{X^{-1}}, \tag{T3.2}
$$
where $B_S$ are the rows of $B$ in $S$ and $S^c$ the complement. $\sigma_S>0$ if and only if $\lambda_{S^c}\neq0$, i.e.
$\mathcal A_+\not\subseteq S$.

*Proof.* (T3.1): $\lambda_S$ (the exact multiplier with the entries outside $S$ set to zero) is admissible, so
$\Phi(\ell_S)\le\Phi(\lambda_S)$. Its residual is $f+B^T\lambda_S-K\hat u=Ke-B^T\lambda_{S^c}$, and $X^{-1}\preceq\gamma_XK^{-1}$ gives
$\|v\|_{X^{-1}}\le\sqrt{\gamma_X}\|v\|_{K^{-1}}$, so $\bar\rho(\lambda_S)\le s(\|e\|_K+m(S^c))$ (with $\|Ke\|_{K^{-1}}=\|e\|_K$). Also
$\lambda_S^T\hat g\le\lambda^T\hat g$ as all entries are non-negative. Step 2 of Theorem E ($\Delta^{\star2}\le\frac43\Phi$) completes the bound.
(T3.2): for $\ell\ge0$ supported in $S$, $f+B^T\ell-K\hat u=Ke-B^T(\lambda-\ell)$, so
$\sqrt{\alpha_X}\,\Delta^\star(\ell)\ge\|B^T(\lambda-\ell)\|_{X^{-1}}-\|Ke\|_{X^{-1}}$. The first norm is at least $\sigma_S$ (drop the sign constraint
and absorb $\lambda_S-\ell$ into $v$), the second at most $\sqrt{\gamma_X}\|e\|_K$. If $\lambda_{S^c}\neq0$ then $B^T\lambda_{S^c}\notin\operatorname{range}B_S^T$
because $B^T$ has full column rank, so $\sigma_S>0$. $\square$

**Corollary T3.** If $\mathcal A_+\subseteq S$, S1-restricted satisfies exactly the bound (E1) of S1: restricting the support to
$S$ costs nothing in the efficiency bound. If $\mathcal A_+\not\subseteq S$, the certificate has a floor
$\Delta^\star(\ell_S)\ge(\sigma_S-\sqrt{\gamma_X}\|e\|_K)/\sqrt{\alpha_X}$; for a fixed problem and fixed support it tends to $\sigma_S/\sqrt{\alpha_X}>0$ as
$\|e\|_K\to0$, so the certificate does not converge. *(Qualifier added 23 Nov 2026: along sequences in which the problem,
mesh or support changes, non-convergence needs $\sigma_S/\sqrt{\alpha_X}$ bounded away from zero.)*

**Comparison with T1.** Missing a strictly active row costs a half rate in the correction (T1) but the convergence
itself in the multiplier support (T3). The support must therefore be chosen more generously than the snap set.

**Support rule.** Take $S_t:=\{i:\hat g_i\le t\}$. Since $\hat g_i=-(Be)_i$ on $\mathcal A$ (0.1), $\mathcal A_+\setminus S_t\subseteq\{i:|(Be)_i|>t\}$, so
$\|Be\|_\infty\le t$ implies $\mathcal A_+\subseteq S_t$ and the S1 bound. For R0s, $\hat{\mathcal A}\subseteq S_t$ for every $t\ge0$. Because $S_t$ is
built from the corrected gap $\hat g$ (available online), it is a computable rule; its size $|S_t|$ sets the cost of the
restricted LCP (X4).

---

## 4. Summary for the paper (Section "Analysis")

| Result | Statement | Use |
|---|---|---|
| T1 | $\lambda^T\hat g=-\lambda_M^TB\tilde e\le m(M)\min(\|e\|_K,\|\tilde e\|_K)$; crossover $e_\times=m(M)/s^2$ | quantitative E3 for missed rows; sharpness via Proposition E2 |
| T1b | $\lambda^T\hat g\le\|\lambda_M\|_1\max_M\hat g_i$; rate $(1+a)/2$ if $\|\lambda_M\|_1\sim\|e\|^a$ | explains the observed R0 rates between 1/2 and 1; design of the lift-off benchmark ($a\approx0$) |
| T2 | $e_{snap}=e_{R0}+B^+p$, $p=\tilde g^+$ on $\hat{\mathcal A}$; cost $\le\beta\|p\|_2$; gap rule: $\le\beta t|\hat{\mathcal A}_t|^{1/2}$ | explains the multiplier-rule failure; justifies the gap rule |
| T2c | $\|B\tilde e\|_\infty\le t\Rightarrow$ full rate and bounded cost | the threshold trade-off of X3 |
| T3 | S1-restricted: same bound as S1 if $\mathcal A_+\subseteq S$; $O(1)$ floor otherwise | support rule $S_t=\{\hat g\le t\}$ for X4 |

---

## 5. Numerical checks

Unit tests (`tests/test_theory.py`, all passing): Proposition E2 example with $\sqrt{\varepsilon/2}\le\Delta^\star\le\frac2{\sqrt3}(\varepsilon^2+\varepsilon)^{1/2}$ for
$\varepsilon\in\{0.5,\dots,10^{-4}\}$; (T1.1) as an identity and bound, (T1.2), R0 = R0s with $\hat{\mathcal A}=\emptyset$; (T2.1) identity and
$\beta$ against a dense eigenvalue; (T3.1), and the floor (T3.2) at $\hat u=u$ with one strictly active row removed from $S$.

Benchmark checks (`experiments/check_theory.py`, seed 0, 100 test queries × all X1 basis sizes, $X=K(\bar\mu)$, S1;
R0s with the gap rule $t=10^{-3}\,\mathrm{char\_gap}$; results in `results/theory/<problem>_seed0.npz`, run 23 Nov 2026):

| | membrane | block | layered |
|---|---|---|---|
| violations of (T1.1), (T1.2), (T2.1), (T2.3) | 0 % | 0 % | 0 % |
| R0: queries with missed rows; median $\lvert M\rvert$ | 100 %; 14 | 94 %; 5 | 91 %; 11 |
| R0: median $m(M)/\|e\|_K$ | 16.5 | 4.0 | 2.7 |
| R0: tightness of (T1.1) / of (T1.5), median | 0.04 / 0.23 | 0.24 / 0.59 | 0.21 / 0.56 |
| R0: excess $\sim\|e\|^q$; $\|\lambda_M\|_1\sim\|e\|^a$ | $q=1.38$; $a=0.32$ | $q=1.51$; $a=0.88$ | $q=1.23$; $a=0.58$ |
| R0: median effectivity, lowest → highest tercile of $m(M)/\|e\|_K$ | 1.26 → 1.69 | 1.23 → 2.02 | 1.19 → 2.01 |
| R0s (gap): queries with missed rows; excess $\sim\|e\|^q$ | 76 %; $q=1.99$ | 85 %; $q=1.47$ | 84 %; $q=1.53$ |
| T2: median change of the error by snapping, gap / multiplier rule | −0.5 % / +392 % | −0.2 % / +379 % | 0.0 % / +311 % |
| T2: (T2.3) bound / actual cost, median | 53 | 79 | 58 |
| T3: $S_t$ ($t$ as above) covers $\mathcal A_+$ | 24 % | 15 % | 16 % |
| T3: median $\Delta^\star(\ell_{S_t})/\Delta^\star(\ell_{S1})$, covered / not covered | 1.000 / 1.27 | 1.000 / 1.43 | 1.000 / 1.20 |

Reading:
1. All bounds hold on every query. The effectivity increases with $m(M)/\|e\|_K$ as (T1.3) predicts, but (T1.3) is
   conservative by a factor 2–10; the localized form (T1.5) is tighter by a factor 3–6.
2. The near-full R0 rates of Gate 0 are explained by Corollary T1b ($a>0$), not by the crossover (T1.4); Remark 2 of
   Section 1 is corrected accordingly.
3. T2 confirms the design rule: the gap rule changes the error by less than 1 %, the multiplier rule increases it
   three- to fourfold. The a priori bound (T2.3) is valid but loose (factor 50–80); it is useful as a guarantee, not
   as an estimate.
4. T3: with the tight snap threshold, $S_t$ covers $\mathcal A_+$ in only 15–24 % of the queries; where it does, the
   restricted certificate equals S1 to three digits, as Corollary T3 states; where it does not, it is 20–43 % larger.
   The support threshold must therefore be larger than the snap threshold (X4, weeks 5–6).
