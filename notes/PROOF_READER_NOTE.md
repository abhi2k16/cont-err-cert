# Request for an independent reading of the proofs

*Cover note for a mathematical reader. Placeholders in [brackets] are to be filled in by the author before sending.*

Dear [name],

thank you for considering a read of a short manuscript, *Efficiency and limitations of optimised-multiplier error certificates for discrete contact problems*
(18 pages, draft of 23 November 2026, no venue chosen). I am asking for an independent check of the mathematics, not of the language or the numerical work.

## What the paper does

For the discrete frictionless contact problem K u − Bᵀλ = f, g = B u − c ≥ 0, λ ≥ 0, λᵀg = 0 (K symmetric positive definite, B of full row rank), and a feasible
approximation û with gap ĝ = B û − c ≥ 0, the error is bounded by a known "feasible-pair" certificate Δ\*(ℓ) = ½(ρ + √(ρ² + 4 ℓᵀĝ)), where ρ is a residual norm of the pair
(û, ℓ) and ℓ ≥ 0 is a free multiplier (Repin; Braess; Zhang, Bader and Veroy). We study the multiplier that minimises the convex surrogate ρ² + ℓᵀĝ, which is a linear
complementarity problem. The claims are:

1. an efficiency bound of Δ\* in terms of the true error and λᵀĝ (Theorem 3.1), which for X = K is a modest extension of the primal–dual gap identity (Remark 3.4);
2. for X = K, the minimiser is the solution multiplier of a contact problem with obstacle c + ĝ/2, and equals λ if and only if 0 ≤ ĝ ≤ 2g, in which case the certificate equals the error (Proposition 3.5, Corollary 3.6);
3. an explicit example in which no multiplier avoids a square-root loss (Proposition 4.1);
4. bounds through the strictly active rows that û leaves open (Theorem 4.2, Corollary 4.3);
5. a multiplier restricted to a support that omits a strictly active row has a floor that does not decrease with the error (Theorem 4.4).

The certificate, its surrogate and the gap identities are known; the paper does not claim them. Section 6 (corrections of reduced-order predictions) is an application and is not part of the request.

## What I would like you to check

Please re-derive the proofs yourself, before reading anything else I provide:

| Where | Statements |
|---|---|
| `paper/sections/02_setting.tex` | Proposition 2.1 (established certificate, included for completeness), Lemma 2.2, Proposition 2.3 |
| `paper/sections/03_analysis.tex`, Section 3 | Theorem 3.1, Remark 3.2, Corollary 3.3, Remark 3.4, Proposition 3.5, Corollary 3.6 |
| `paper/sections/03_analysis.tex`, Section 4 | Proposition 4.1, Theorem 4.2, Corollary 4.3, Theorem 4.4 |

For each statement, a verdict (correct / needs an additional assumption / gap in the proof / false) and the step you doubt would be ideal. I am equally interested in:
(a) hidden assumptions (uniqueness, X = K versus a general inner product, full row rank of B versus injectivity of Bᵀ);
(b) statements in the Introduction and Section 7 that claim more than is proved;
(c) whether Remark 3.4 and the attribution to Repin (2000, 2007), Braess (2005), Krause–Veeser–Walloth (2015), Bartels et al. (2025) and Repin–Valdman (2018) are fair.

## What has been done, and what has not

- **Numerical evidence** (Section 5): three experiments; every statement above was tested on random instances (3 × 1000, no violations beyond 10⁻⁹) and the exactness, floor and half-rate statements on finite element
  queries and a controlled sequence. Tests of this kind do not replace a proof, and four protocol adjustments made after the first runs are disclosed in Section 5.4.
- **A previous check**: an independent AI model re-derived the proofs in an earlier version. It found one false inequality (Corollary 4.3, a norm comparison), which has been corrected; please do not take the rest as verified on that basis.
- **Literature**: two sources, Chen and Nochetto (*Numer. Math.* 84, 2000) and Repin's 2009 ENUMATH paper, could not be obtained and were not read; several others were read only as preprints. If you know of earlier work that contains the efficiency bound, the exactness condition or the half-rate example in equivalent form, that is the most valuable thing you could tell me.

## Optional, after your own pass

`PROOF_AUDIT_GUIDE.md` lists, per statement, the assumptions used and where I suspect an error could hide; it also lists a few questions I would like your view on. I suggest reading it last so that it does not steer your reading.

## Time and format

I estimate half a day for the proofs. Any format is fine: marked-up PDF, a list by statement number, or a short email. If you find the results too slight or too close to known work to merit a paper, please say so; that judgement is as useful to me as a list of errors.

## Material

`main.pdf` (18 pages), the sources in `paper/sections/`, `PROOF_AUDIT_GUIDE.md`, and, if wanted, the code and results in `certified-correction-contact-rom/` (README: "Reproducing the short paper").

With thanks,
[author name and affiliation]
