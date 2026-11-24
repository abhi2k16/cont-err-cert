<h1 align="center">certificate-efficiency</h1>

<p align="center">
  <b>How sharp are optimized-multiplier error certificates for discrete contact problems?</b><br>
  Numerical studies of active-set consistency, exact certification, restricted multiplier support and worst-case degradation.
</p>

<p align="center">
  <img alt="Python 3.10+" src="https://img.shields.io/badge/python-3.10%2B-3776AB?logo=python&logoColor=white">
  <img alt="NumPy" src="https://img.shields.io/badge/NumPy-2.2.6-013243?logo=numpy&logoColor=white">
  <img alt="SciPy" src="https://img.shields.io/badge/SciPy-1.15.3-8CAAE6">
  <img alt="Problem class" src="https://img.shields.io/badge/problem-frictionless%20unilateral%20contact-orange">
  <img alt="Benchmarks" src="https://img.shields.io/badge/benchmarks-membrane%20%7C%20block-teal">
  <a href="LICENSE"><img alt="License MIT" src="https://img.shields.io/badge/license-MIT-green"></a>
</p>

<p align="center">
  <a href="#problem-and-scope">Problem</a> ·
  <a href="#numerical-studies">Studies</a> ·
  <a href="#quick-start">Quick start</a> ·
  <a href="#saved-results">Results</a> ·
  <a href="#repository-layout">Layout</a>
</p>

---

## Problem and scope

A posteriori error certificates for discrete frictionless contact problems depend on both a feasible approximation and a compatible
multiplier. This project examines how certificate efficiency relates to active-set consistency, when exact certification occurs, and
how missed contact constraints or restricted multiplier support affect the bounds.

This repository is a research snapshot of experiment scripts and saved numerical outputs. It does not include the manuscript, research
notes, literature PDFs or the `certcorrect` package. The scripts also rely on the authors' local `fea_engine` and `rom_engine` packages.

## Numerical studies

| Study | Question | Saved output |
|---|---|---|
| **E1 - Exactness** | When does the certificate equal the true energy error for finite-element queries? | `results/e1_exactness/` |
| **E2 - Support floor** | How does restricting multiplier support affect the certificate on a controlled lift-off sequence? | `results/e2_support_floor/` |
| **E3 - Random instances** | Do the derived certificate properties hold across random inequality-constrained systems? | `results/e3_random/` |
| **Half-rate example** | Does the two-dimensional example exhibit square-root certificate degradation? | `results/e_halfrate/` |

The finite-element studies use membrane and block benchmarks. Seeds 0, 1 and 2 are included for the seeded experiments. The `code/`
directory contains the corresponding experiment scripts plus helpers for generating tables and figures from saved summaries.

## Quick start

The pinned numerical dependencies are listed in `requirements.txt`:

```bash
python -m venv .venv
python -m pip install -r requirements.txt
```

Installing these requirements alone is not sufficient to run the experiment scripts: they import `certcorrect`, `fea_engine` and
`rom_engine`, which are not included in this repository. Run the scripts from the full source checkout with its configured Python
environment. For example:

```bash
python experiments/e1_exactness.py --problem membrane --seed 0
python experiments/e2_support_floor.py --problem membrane --seed 0
python experiments/e3_random_instances.py --seed 0 --n-instances 1000
python experiments/e_halfrate.py
```

## Saved results

`results/` contains NPZ arrays and JSON summaries for the completed runs:

| Folder | Contents |
|---|---|
| `results/e1_exactness/` | E1 outputs for membrane and block, seeds 0-2 |
| `results/e2_support_floor/` | E2 support-floor runs and restricted-multiplier diagnostics |
| `results/e3_random/` | Random-instance verification summaries, seeds 0-2 |
| `results/e_halfrate/` | Half-rate example arrays and summary |

The `tables.py` and `figures.py` scripts in `code/` use the saved results to generate the associated manuscript tables and figures in
the full source checkout.

## Repository layout

```text
code/
├── e1.py          finite-element exactness study
├── e2.py          restricted multiplier support-floor study
├── e2_mult.py     multiplier diagnostic
├── e3.py          random-instance verification
├── halfrate.py    square-root degradation example
├── tables.py      table generation from saved summaries
└── figures.py     figure generation from saved results
results/
├── e1_exactness/
├── e2_support_floor/
├── e3_random/
└── e_halfrate/
requirements.txt
LICENSE
```

## License and citation

Released under the MIT License; see [LICENSE](LICENSE). The manuscript and citation details are maintained outside this repository.
