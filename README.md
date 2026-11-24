# certificate-efficiency

Everything relevant to the manuscript **Efficiency and limitations of optimised-multiplier error certificates for discrete contact problems**, in one place.

This folder is a **copy**. The originals stay where they are and are authoritative:
the code repository `../admissible-lifting-certification/certified-correction-contact-rom/` (git; package, tests, experiments, results, paper), the notes in `../admissible-lifting-certification/` and the PDFs in `../admissible-lifting-certification/literatures/`.
After changing an original, refresh this folder with `bash sync_from_repo.sh`. Do not edit files here; edits are overwritten by the next sync.

## Contents

| Folder | What it holds |
|---|---|
| `manuscript/` | LaTeX sources (`main.tex`, `sections/`, `macros.tex`, `refs.bib`), generated `tables/`, the three `figures/` used, and the built `main.pdf` |
| `code/` | The seven scripts of the current line: `e1.py`, `e2.py`, `e2_mult.py`, `e3.py`, `halfrate.py` (experiments) and `tables.py`, `figures.py` (tables and figures from saved results) |
| `results/` | Saved results of those experiments: `e1_exactness/`, `e2_support_floor/`, `e3_random/`, `e_halfrate/` (NPZ arrays and JSON summaries; 3 seeds) |
| `notes/` | `RESEARCH_RECORD.md` (start here), `PROOF_AUDIT_GUIDE.md`, `PROOF_READER_NOTE.md` (cover note for a proof reader), `CLAIM_SHEET.md`, `CLAIM_SHEET_AUDIT_RESULTS.md` (literature audit), `THEOREM_certificate_efficiency.md`, `ANALYSIS_T1_T3.md`, `SHORT_PAPER_SCOPE.md` (previous scope file with the pre-registered criteria and dated log) |
| `literature/` | PDFs of the sources relevant to the manuscript (the two PDFs belonging to closed lines are left out) |

## Where to start

1. `notes/RESEARCH_RECORD.md`: question, claims with theorem numbers, mathematical map, evidence, literature status, verification history, open items.
2. `manuscript/main.pdf`: the current draft (16 pages).
3. `notes/PROOF_READER_NOTE.md` with `notes/PROOF_AUDIT_GUIDE.md`: material for an independent mathematical reader.

## Build the manuscript

```bash
cd manuscript
latexmk -pdf -outdir=build main.tex
```

The copy is self-contained: it builds without the code repository (checked on 24 Nov 2026: 16 pages, no errors, no undefined references).

## Re-run the experiments

The scripts in `code/` import the package `certcorrect` and the engines `fea_engine`, `rom_engine`, which live in the code repository (project `.venv`), so they are run from there:

```bash
cd ../admissible-lifting-certification/certified-correction-contact-rom
for s in 0 1 2; do
  for p in membrane block; do
    python experiments/e1.py --problem $p --seed $s
    python experiments/e2.py --problem $p --seed $s
    python experiments/e2_mult.py --problem $p --seed $s
  done
  python experiments/e3.py --seed $s --n-instances 1000
done
python experiments/halfrate.py
python experiments/tables.py
python experiments/figures.py
```

then `bash ../../certificate-efficiency/sync_from_repo.sh` to refresh this folder.

## Status (24 Nov 2026)

Numerical evidence passed as reported; proofs checked by two independent AI audits (one false inequality found and fixed), no human reader yet; literature closure accepted with residual risk (two sources unread); publication decision pending. Details: `notes/RESEARCH_RECORD.md`.
