#!/usr/bin/bash
#
# Run the whole set of quantitative benchmarks
#

OUT_PREFIX="results"

mkdir -p "$OUT_PREFIX"

## Quantitative

python3 memusage.py ./pvesta.sh eventual > "$OUT_PREFIX/pvesta-eventual.out" 2> "$OUT_PREFIX/pvesta-eventual.err"
python3 memusage.py ./pvesta.sh strong > "$OUT_PREFIX/pvesta-strong.out" 2> "$OUT_PREFIX/pvesta-strong.err"

python3 memusage.py ./multivesta.sh eventual > "$OUT_PREFIX/multivesta-eventual.out" 2> "$OUT_PREFIX/multivesta-eventual.err"
python3 memusage.py ./multivesta.sh strong > "$OUT_PREFIX/multivesta-strong.out" 2> "$OUT_PREFIX/multivesta-strong.err"

./mc2.sh eventual 60 > "$OUT_PREFIX/mc2-eventual.out" 2> "$OUT_PREFIX/mc2-eventual.err"
./mc2.sh strong 7380 > "$OUT_PREFIX/mc2-strong.out" 2> "$OUT_PREFIX/mc2-strong.err"
