# Efficiency of the feasible-pair certificate with an optimised multiplier

Result (1) of the v6 formulation, worked out as a theorem with proof, plus a sharpness example and a constructive consequence; followed by a comparison with Haasdonk–Salomon–Wohlmuth (2012) and Zhang–Bader–Veroy (2014/2016). Written 22 Nov 2026.

Notation as in MATH_FORMULATION_v6c.md: $K\succ0$, $B$ full row rank, $(u,\lambda)$ the full-order solution of $Ku-B^T\lambda=f$, $g=Bu-c\ge0$, $\lambda\ge0$, $\lambda^Tg=0$. A feasible approximation $\hat u$ ($\hat g=B\hat u-c\ge0$), error $e=u-\hat u$. Inner-product matrix $X\succ0$ with constants
$$
\alpha_X\,v^TXv\ \le\ v^TKv\ \le\ \gamma_X\,v^TXv\qquad\forall v .
$$
For $\mu\ge0$ (multiplier variable; written $\ell$ below to avoid confusion with the parameter) define
$$
\bar\rho(\ell)=\frac{\|f+B^T\ell-K\hat u\|_{X^{-1}}}{\sqrt{\alpha_X}},\qquad \eta_c(\ell)=\ell^T\hat g,\qquad
\Delta^\star(\ell)=\tfrac12\Big(\bar\rho+\sqrt{\bar\rho^2+4\eta_c}\Big),
$$
and the S1 surrogate $\Phi(\ell)=\bar\rho(\ell)^2+\eta_c(\ell)$, with $\ell_{S1}=\arg\min_{\ell\ge0}\Phi(\ell)$ (unique; Proposition 1 of MATH_FORMULATION_v6c).

---

## Theorem E (two-sided bound for the S1 certificate)

For every feasible $\hat u$,
$$
\|e\|_K\ \le\ \Delta^\star(\ell_{S1})\ \le\ \frac{2}{\sqrt3}\sqrt{\Phi(\ell_{S1})}\ \le\ \frac{2}{\sqrt3}\Big(\frac{\gamma_X}{\alpha_X}\|e\|_K^2+\lambda^T\hat g\Big)^{1/2}, \tag{E1}
$$
where $\lambda$ is the exact full-order multiplier, and
$$
0\ \le\ \lambda^T\hat g\ =\ -\lambda^TBe\ \le\ \|B^T\lambda\|_{K^{-1}}\,\|e\|_K . \tag{E2}
$$
The quantity $\|B^T\lambda\|_{K^{-1}}=\|u-K^{-1}f\|_K$ is the energy distance between the constrained and the unconstrained full-order solutions (a measure of contact intensity).

**Proof.**
1. *Lower bound.* $\Delta^\star(\ell)\ge\|e\|_K$ for every $\ell\ge0$ by the feasible-pair certificate (Theorem 1 of MATH_FORMULATION_v6c with (2.3) there).
2. *Exact certificate versus surrogate* (this step is Zhang 2016, Prop. 3.4.1). For $\rho,\eta\ge0$ with $\rho^2+\eta\le P$:
$$
\tfrac12\big(\rho+\sqrt{\rho^2+4\eta}\big)\le\tfrac12\big(\rho+\sqrt{4P-3\rho^2}\big)\le\tfrac{2}{\sqrt3}\sqrt P ,
$$
the last step by maximising $h(\rho)=\rho+\sqrt{4P-3\rho^2}$ on $[0,\sqrt P]$: $h'(\rho)=0$ gives $\rho=\sqrt{P/3}$ and $h=4\sqrt{P/3}$. With $\rho=\bar\rho(\ell_{S1})$, $\eta=\eta_c(\ell_{S1})$, $P=\Phi(\ell_{S1})$ this is the second inequality of (E1).
3. *Comparison with the exact multiplier.* $\ell=\lambda\ge0$ is admissible in the S1 problem, so $\Phi(\ell_{S1})\le\Phi(\lambda)$. At $\ell=\lambda$, $f+B^T\lambda-K\hat u=Ku-K\hat u=Ke$, hence
$$
\bar\rho(\lambda)^2=\frac{e^TKX^{-1}Ke}{\alpha_X}\le\frac{\gamma_X}{\alpha_X}\,e^TKe ,
$$
because $K\preceq\gamma_XX$ is equivalent to $X^{-1}\preceq\gamma_XK^{-1}$, i.e. $KX^{-1}K\preceq\gamma_XK$. Adding $\eta_c(\lambda)=\lambda^T\hat g$ gives the third inequality of (E1).
4. *(E2).* $\hat g=B\hat u-c=g-Be$ and $\lambda^Tg=0$, so $\lambda^T\hat g=-\lambda^TBe=-(B^T\lambda)^Te\le\|B^T\lambda\|_{K^{-1}}\|e\|_K$ by Cauchy–Schwarz in the $K$ / $K^{-1}$ pairing; $\lambda^T\hat g\ge0$ since both factors are non-negative. Finally $B^T\lambda=Ku-f=K(u-K^{-1}f)$ gives $\|B^T\lambda\|_{K^{-1}}=\|u-K^{-1}f\|_K$. $\square$

### Corollary E1 (effectivity and rate)

Let $\mathrm{eff}=\Delta^\star(\ell_{S1})/\|e\|_K$ for $e\neq0$.
- (a) General feasible $\hat u$: $1\le\mathrm{eff}\le\frac{2}{\sqrt3}\big(\frac{\gamma_X}{\alpha_X}+\frac{\|B^T\lambda\|_{K^{-1}}}{\|e\|_K}\big)^{1/2}$. As $\|e\|_K\to0$ the certificate is $O(\|e\|_K^{1/2})$.
- (b) **Active-set consistency.** If $\hat g_i=0$ for every $i$ with $\lambda_i>0$, then $\lambda^T\hat g=0$ and
$$
1\le\mathrm{eff}\le\frac{2}{\sqrt3}\sqrt{\frac{\gamma_X}{\alpha_X}} . \tag{E3}
$$
The certificate then converges at the rate of the error. For $X=K$: $\mathrm{eff}\le 2/\sqrt3\approx1.155$. For $X=I$ (Euclidean, as in M2): $\mathrm{eff}\le(2/\sqrt3)\sqrt{\kappa(K)}$.
- (c) More generally, if $\lambda^T\hat g\le C\|e\|_K^2$, then $\mathrm{eff}\le\frac{2}{\sqrt3}\sqrt{\gamma_X/\alpha_X+C}$.

*Proof.* Divide (E1) by $\|e\|_K$ and use (E2), respectively $\lambda^T\hat g=0$, respectively the assumption. $\square$

### Proposition E2 (the half rate is intrinsic to the certificate class)

Without active-set consistency, no choice of multiplier removes the half rate. Example: $N=n_c=1$, $K=1$, $B=1$, $c=0$, $f=-1$. Then $u=0$, $\lambda=1$, $g=0$. Take the feasible $\hat u=\varepsilon\in(0,\tfrac12]$; $\|e\|_K=\varepsilon$, $\hat g=\varepsilon$. With $X=K$ ($\alpha_X=1$), for every $\ell\ge0$: $\bar\rho(\ell)=|\ell-1-\varepsilon|$ and $\Delta^\star(\ell)\ge\max(\bar\rho,\sqrt{\ell\varepsilon})$. If $\ell\ge(1+\varepsilon)/2$ then $\Delta^\star\ge\sqrt{\varepsilon/2}$; otherwise $\Delta^\star\ge\bar\rho\ge\tfrac12$. Hence
$$
\inf_{\ell\ge0}\Delta^\star(\ell)\ \ge\ \sqrt{\varepsilon/2}\quad\text{and}\quad \inf_{\ell\ge0}\frac{\Delta^\star(\ell)}{\|e\|_K}\ \ge\ \frac{1}{\sqrt{2\varepsilon}}\ \to\infty .
$$
The cause is a row that is in contact in the truth ($\lambda>0$) but open in the approximation ($\hat g>0$). $\square$

*Sharpened 23 Nov 2026 (external audit, verified numerically and by proof):* the optimum is $\min_{\ell\ge0}\Delta^\star(\ell)=\sqrt{\varepsilon(1+\varepsilon)}$,
attained at $\ell=1+\varepsilon$; the paper states the example with $N=2$, $K=I$, $B=[1\ 0]$, $f=(-1,0)^T$ so that $n_c<N$ (paper
Proposition 3.3). Corollary E1(a) is an upper rate; the paper words it as "at worst of order $\|e\|^{1/2}$, sharp in the
worst case".

Consequence: the sharpness of the certificate is controlled by the *approximation* $\hat u$, not by the multiplier optimisation. This turns the correction design into a certificate-design question.

### Proposition E3 (snap-to-contact repair restores the full rate)

Let $\hat{\mathcal A}\subseteq\{1,\dots,n_c\}$ be a predicted active set (for example rows with $\tilde\lambda_i>0$, or with $(B\tilde u-c)_i\le\theta_{snap}$). Define
$$
d_i=\begin{cases}c_i-(B\tilde u)_i,& i\in\hat{\mathcal A}\ \text{(of either sign)},\\ \max\big(0,\,c_i-(B\tilde u)_i\big),& i\notin\hat{\mathcal A},\end{cases}\qquad
\hat u_{snap}=\tilde u+B^+d .
$$
Then $\hat g\ge0$, $\hat g_i=0$ for $i\in\hat{\mathcal A}$, and if $\mathcal A_+:=\{i:\lambda_i>0\}\subseteq\hat{\mathcal A}$, the bound (E3) holds.

*Proof.* $BB^+=I$ gives $\hat g=B\tilde u+d-c$: zero on $\hat{\mathcal A}$ and $\max(B\tilde u-c,0)\ge0$ elsewhere. If $\mathcal A_+\subseteq\hat{\mathcal A}$ then $\lambda^T\hat g=\sum_{i\in\mathcal A_+}\lambda_i\hat g_i=0$; apply Corollary E1(b). $\square$

Remarks.
- Over-predicting the active set ($\hat{\mathcal A}\supsetneq\mathcal A_+$) does not affect (E3), but it can increase $\|e\|_K$ (rows pulled onto the obstacle that should be open). Under-predicting it reintroduces the term $\lambda^T\hat g$ on the missed rows, of size $\sum_{i\in\mathcal A_+\setminus\hat{\mathcal A}}\lambda_i\hat g_i$.
- For Candidate B, the same effect is obtained by adding the equality constraints $(BZ\,\delta q)_i=(c-B\tilde u)_i$, $i\in\hat{\mathcal A}$, to the QP; feasibility then needs $BZ$ restricted to $\hat{\mathcal A}$ to have full row rank, or the augmented basis $[Z\ R]$.
- The result gives a design rule: a correction that is exactly active on a superset of the true strongly active set yields a certificate with effectivity bounded by $\frac2{\sqrt3}\sqrt{\gamma_X/\alpha_X}$, uniformly in the size of the error.

---

## Comparison with the existing bounds

### Haasdonk, Salomon, Wohlmuth (SINUM 50, 2012), Section 4 (read in full, pp. 2665–2668)
- Prop. 4.2 (upper bound): $\|u-u_N\|_V\le c_1+\sqrt{c_1^2+c_2}$, with residual quantities $\delta_r$ (equality residual), $\delta_{s1}=\|\pi(\eta_s)\|$, $\delta_{s2}=(\lambda_N,\pi(\eta_s))$ built from a projection $\pi$ onto the dual cone. The approximation $u_N$ need not be feasible; the multiplier is the RB multiplier $\lambda_N$, not optimised.
- Prop. 4.4 (lower bounds): $\delta_r\le\gamma_a\|u-u_N\|+\gamma_b\|\lambda-\lambda_N\|$, $\delta_{s1},\delta_{s2}\lesssim\|u-u_N\|$.
- Remark 4.5: "In the upper bound the term $\sqrt{\delta_{s2}}$ enters, whereas in the lower bound the term $\delta_{s2}$ appears. This results from the variational inequality setting."
- Remark 4.6 and the closing comment: the lower bounds depend on $C_\pi/c_\pi$ and the estimator is not fully offline–online decomposable.

What is already known from HSW: the square-root gap between upper and lower bound, i.e. the half-rate phenomenon, is identified (Remark 4.5). Their residual lower bound contains the **dual** error $\|\lambda-\lambda_N\|$ because $\lambda_N$ is fixed.

What HSW does not contain (in the sections read): an upper bound of the whole certificate by the **primal** error alone (obtained here by optimising the multiplier and comparing with the exact $\lambda$); a condition under which the gap disappears; a proof that the gap is attained for every multiplier choice; the snap-to-contact construction.

### Zhang, Bader, Veroy (arXiv 1410.2095, 2014; C. R. Math. 354, 2016)
- Prop. 4.3: for the strictly feasible primal-dual pair $(u_n^{du},\lambda_n^{pr})$, $\|u-u_n\|_V\le\tilde d_1+\sqrt{\tilde d_1^2+\tilde d_2}$ with $\tilde d_1=\|r\|_{V'}/(2\alpha)$, $\tilde d_2=\langle s_n,\lambda_n\rangle/\alpha$. This is the feasible-pair certificate (Theorem 1 of MATH_FORMULATION_v6c) in the same quadratic-root form. **So Theorem 1, including the sharp form, is already in Zhang–Bader–Veroy.**
- Rate: the introduction states that the HSW bound "does not mimic the actual convergence rate" and that the duality approach "provides sharp error bounds that mimic the convergence rate". In the parts read, this is supported by the numerical results (Sec. 6, "mimics the true convergence rate"), not by a theorem. The multiplier is the primal RB multiplier $\lambda_n^{pr}$, not optimised; no lower bound or effectivity bound is stated in the parts read.

What Theorem E adds relative to Zhang–Bader–Veroy: a proof of when such a certificate converges at the full rate (Corollary E1(b),(c)), a quantitative effectivity bound, and a proof that without active-set consistency the half rate cannot be avoided by any multiplier (Proposition E2). Theorem E offers an explanation of their numerical observation, if their slack approximation keeps $\langle s_n,\lambda\rangle$ of order $\|e\|^2$; this is a conjecture, not checked.

### Zhang, *Certified Reduced Basis Method for Variational Inequalities*, PhD dissertation, RWTH Aachen 2016 (read 22 Nov 2026: Sec. 1.4, 3.2.3, 3.3.3–3.3.5, 3.4 in full, 4.3 numerical discussion, Ch. 6; full text searched for "effectiv", "rate", "lower bound", "projection")
- Sec. 3.3.3: slack approach for surjective $B$ via $V=\ker B\oplus(\ker B)^\perp$, $B_\perp$ bijective on $(\ker B)^\perp$; Sec. 4.3.2: $P_\perp=B^T(BB^T)^{-1}B$. **Baseline A is this method.**
- Prop. 3.3.6: feasible-pair bound $d_1+\sqrt{d_1^2+d_2}$, $d_1=\|r\|_{V'}/(2\alpha)$, $d_2=\langle s_n,\lambda_n\rangle/\alpha$ (same as Zhang–Bader–Veroy Prop. 4.3).
- **Prop. 3.4.1:** $\dfrac{\|r\|^2_{V'}+\alpha\langle s_n,\lambda_n\rangle}{\alpha^2}\le\Delta_u^2\le\dfrac43\,\dfrac{\|r\|^2_{V'}+\alpha\langle s_n,\lambda_n\rangle}{\alpha^2}$. **This is step 2 of the proof of Theorem E, including the constant $2/\sqrt3$, and the matching lower bound $\Delta^{\star2}\ge\Phi$.**
- **Problems (3.123)–(3.124), $P_n^{sl\text{-}min}$:** $\lambda_n^{min}=\arg\min_{q\ge0}\|r(s_n,q)\|^2_{V'}+\alpha\langle s_n,q\rangle$. **This is S1** (up to the factor $\alpha$). Problems (3.126)–(3.127) minimise jointly over slack and multiplier (the "minimum residual approach").
- Prop. 3.3.5: a priori quasi-optimality of the slack solution, $\|u-u_n\|\le\big(\frac{\gamma^2}{\alpha^2}\|u-v_n\|^2+\frac2\alpha\|f-Au\|_{V'}\|u-v_n\|\big)^{1/2}$, i.e. order $1/2$ for the *solution* (not the certificate).
- Rate of the bounds: stated only numerically ("follow the convergence rate of the approximation", Sec. 4.3.3).
- Not found: a bound of the certificate in terms of the true error; any condition for full-rate certification; a lower bound showing the half rate is unavoidable; any post-solve correction of a primal (Galerkin) ROM solution. The primal approach is handled by replacing it with the slack ROM, and its infeasibility enters only through the projection $\Pi$ in the HSW estimator.

---

## Verdict

| Part | Status |
|---|---|
| Feasible-pair certificate, quadratic-root form | Known (Zhang–Bader–Veroy Prop. 4.3; Zhang thesis Prop. 3.3.6) |
| Square-root gap between upper and lower bounds | Known as an observation (HSW Remark 4.5) |
| S1 multiplier (minimum residual) | Known (Zhang thesis (3.123)–(3.124)) |
| Step 2 of Theorem E: $\Phi\le\Delta^{\star2}\le\frac43\Phi$ | Known (Zhang thesis Prop. 3.4.1) |
| Step 3 of Theorem E: $\Phi(\ell_{S1})\le\frac{\gamma_X}{\alpha_X}\|e\|_K^2+\lambda^T\hat g$, hence the certificate bounded by the true primal error (efficiency) | Not found in HSW, Zhang–Bader–Veroy or the Zhang thesis |
| Corollary E1(b),(c): active-set consistency gives full rate and effectivity $\le\frac2{\sqrt3}\sqrt{\gamma_X/\alpha_X}$ | Not found; explains the numerical rate observations of Zhang et al. (conjecture for their slack ROM) |
| Proposition E2: half rate attained for every multiplier | Not found |
| Proposition E3: snap-to-contact post-solve repair with full-rate guarantee | Not found; no post-solve correction of a Galerkin ROM appears in any of the three sources |

Theorem E should be presented as: Zhang's Prop. 3.4.1 and minimum-residual multiplier (cited) combined with a new comparison argument (step 3) that turns them into an efficiency bound in the true error. The new contribution is step 3 together with Corollary E1, Proposition E2 and Proposition E3: the certificate's rate is governed by active-set consistency of the approximation, the half rate is otherwise unavoidable, and a post-solve repair achieves consistency.

Open checks:
1. Zhang thesis Ch. 5 (parabolic) not read in full; the search found no efficiency statement there.
2. Zhang–Bader–Veroy 2014 read in part; the thesis supersedes it.
3. Numerically test (E3) and Proposition E2 on the membrane (snap versus plain R0, effectivity against error).
