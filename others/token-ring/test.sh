./run.sh -smc off -tr tokenring.maude init-tokenring.maude pi-tokenring.maude

rm -rf output.txt
maude -no-banner test.maude > output