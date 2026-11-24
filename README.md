# certificate-efficiency

Experiment scripts and numerical results for the manuscript **Efficiency and limitations of optimised-multiplier error certificates for discrete contact problems**.

This folder is a **copy**. The originals stay where they are and are authoritative: the code repository `../admissible-lifting-certification/certified-correction-contact-rom/` (git; package, tests, experiments, results, paper), the notes in `../admissible-lifting-certification/` and the PDFs in `../admissible-lifting-certification/literatures/`. The public repository tracks the experiment code and results; manuscript sources, research notes and literature PDFs are intentionally not included. After changing an original, refresh this local folder with `bash sync_from_repo.sh`.

## Contents

| Folder | What it holds |
|---|---|
| `code/` | The seven scripts of the current line: `e1.py`, `e2.py`, `e2_mult.py`, `e3.py`, `halfrate.py` (experiments) and `tables.py`, `figures.py` (tables and figures from saved results) |
| `results/` | Saved results of those experiments: `e1_exactness/`, `e2_support_floor/`, `e3_random/`, `e_halfrate/` (NPZ arrays and JSON summaries; 3 seeds) |

## Where to start

Start with the experiment scripts in `code/` and the saved outputs in `results/`. The manuscript and supporting research materials are maintained outside this repository.

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

then `bash ../../certificate-efficiency/sync_from_repo.sh` to refresh the local copy.

## Status (24 Nov 2026)

Numerical evidence passed as reported; proofs checked by two independent AI audits (one false inequality found and fixed), no human reader yet; literature closure accepted with residual risk (two sources unread); publication decision pending. Detailed research notes are maintained outside this repository.
