#!/usr/bin/env bash
# Rebuilds this folder as a self-contained copy of everything relevant to the manuscript
#   "Efficiency and limitations of optimised-multiplier error certificates for discrete contact problems".
# The originals (code repo, notes, literature) stay where they are and are authoritative; run this script again after changing them.
# Usage:  bash sync_from_repo.sh        (from this folder or anywhere)
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$HERE/../admissible-lifting-certification" && pwd)"   # project folder with the code repo, notes and literature
REPO="$ROOT/certified-correction-contact-rom"

# empties a folder but tolerates a file that is open in a viewer (it is overwritten below if possible)
fresh() { mkdir -p "$HERE/$1"; find "$HERE/$1" -mindepth 1 -delete 2>/dev/null || true; }

# 1. manuscript: sources, generated tables, the three figures used, bibliography, built PDF
fresh manuscript
cp "$REPO/paper/main.tex" "$REPO/paper/macros.tex" "$REPO/paper/refs.bib" "$HERE/manuscript/"
cp -r "$REPO/paper/sections" "$HERE/manuscript/sections"
cp -r "$REPO/paper/tables" "$HERE/manuscript/tables"
mkdir -p "$HERE/manuscript/figures"
for f in fig_e1_effectivity fig_e2_support_floor fig_halfrate; do
  cp "$REPO/paper/figures/$f.pdf" "$REPO/paper/figures/$f.png" "$HERE/manuscript/figures/"
done
if [ -f "$REPO/paper/build/main.pdf" ]; then
  cp -f "$REPO/paper/build/main.pdf" "$HERE/manuscript/main.pdf" || echo "warning: manuscript/main.pdf is open in a viewer; close it and sync again"
fi

# 2. code: the scripts of the current line (they import the package certcorrect from the code repo)
fresh code
# source name (in the code repo) -> short name (here)
for pair in e1_exactness:e1 e2_support_floor:e2 e2_multiplier_check:e2_mult e3_random_instances:e3 e_halfrate:halfrate e_tables:tables e_figures:figures; do
  cp "$REPO/experiments/${pair%%:*}.py" "$HERE/code/${pair##*:}.py"
done

# 3. results of the current line
fresh results
for d in e1_exactness e2_support_floor e3_random e_halfrate; do
  cp -r "$REPO/results/$d" "$HERE/results/$d"
done

# 4. notes: record, audit material, claim sheets and derivations of the current line, previous scope file
fresh notes
cp "$ROOT/RESEARCH_RECORD.md" "$ROOT/PROOF_AUDIT_GUIDE.md" "$ROOT/PROOF_READER_NOTE.md" "$HERE/notes/"
cp "$ROOT/CLAIM_SHEET.md" "$ROOT/CLAIM_SHEET_AUDIT_RESULTS.md" "$ROOT/THEOREM_certificate_efficiency.md" "$ROOT/ANALYSIS_T1_T3.md" "$HERE/notes/"
cp "$ROOT/archive/SHORT_PAPER_SCOPE.md" "$HERE/notes/"

# 5. literature: sources relevant to the manuscript (the options-pricing and vector-space-sieving PDFs belong to closed lines)
fresh literature
find "$ROOT/literatures" -maxdepth 1 -name '*.pdf' \
  ! -name 'Reduced Basis Methods for Pricing Options*' \
  ! -name 'Online adaptive basis refinement*' \
  -exec cp {} "$HERE/literature/" \;

echo "synced: $(find "$HERE" -type f ! -name sync_from_repo.sh ! -name README.md | wc -l) files"
