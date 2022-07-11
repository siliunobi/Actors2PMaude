./run.sh -smc off -tr fbar.maude init-fbar.maude pi-fbar.maude

rm -rf output.txt
maude -no-banner test.maude > output