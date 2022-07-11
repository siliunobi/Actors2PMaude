./run.sh -smc off -tr aodv.maude init-aodv.maude pi-aodv.maude

rm -rf output.txt
maude -no-banner test.maude > output