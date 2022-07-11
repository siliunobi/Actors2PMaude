rm -rf output5.txt
rm -rf output7.txt
rm -rf output9.txt

java -jar ../../pvesta/pvesta-server.jar > server.out &

java -jar ../../pvesta/pvesta-client.jar -l ../../pvesta/serverlist -m test9-1.maude -f reduction.quatex -a 0.05 >> output9.txt

java -jar ../../pvesta/pvesta-client.jar -l ../../pvesta/serverlist -m test9-2.maude -f reduction.quatex -a 0.05 >> output9.txt

java -jar ../../pvesta/pvesta-client.jar -l ../../pvesta/serverlist -m test9-3.maude -f reduction.quatex -a 0.05 >> output9.txt

java -jar ../../pvesta/pvesta-client.jar -l ../../pvesta/serverlist -m test9-4.maude -f reduction.quatex -a 0.05 >> output9.txt

java -jar ../../pvesta/pvesta-client.jar -l ../../pvesta/serverlist -m test9-5.maude -f reduction.quatex -a 0.05 >> output9.txt

java -jar ../../pvesta/pvesta-client.jar -l ../../pvesta/serverlist -m test9-6.maude -f reduction.quatex -a 0.05 >> output9.txt

python do_read_p_res.py output9.txt


java -jar ../../pvesta/pvesta-client.jar -l ../../pvesta/serverlist -m test7-1.maude -f reduction.quatex -a 0.05 >> output7.txt

java -jar ../../pvesta/pvesta-client.jar -l ../../pvesta/serverlist -m test7-2.maude -f reduction.quatex -a 0.05 >> output7.txt

java -jar ../../pvesta/pvesta-client.jar -l ../../pvesta/serverlist -m test7-3.maude -f reduction.quatex -a 0.05 >> output7.txt

java -jar ../../pvesta/pvesta-client.jar -l ../../pvesta/serverlist -m test7-4.maude -f reduction.quatex -a 0.05 >> output7.txt

java -jar ../../pvesta/pvesta-client.jar -l ../../pvesta/serverlist -m test7-5.maude -f reduction.quatex -a 0.05 >> output7.txt

java -jar ../../pvesta/pvesta-client.jar -l ../../pvesta/serverlist -m test7-6.maude -f reduction.quatex -a 0.05 >> output7.txt

python do_read_p_res.py output7.txt


java -jar ../../pvesta/pvesta-client.jar -l ../../pvesta/serverlist -m test5-1.maude -f reduction.quatex -a 0.05 >> output5.txt

java -jar ../../pvesta/pvesta-client.jar -l ../../pvesta/serverlist -m test5-2.maude -f reduction.quatex -a 0.05 >> output5.txt

java -jar ../../pvesta/pvesta-client.jar -l ../../pvesta/serverlist -m test5-3.maude -f reduction.quatex -a 0.05 >> output5.txt

java -jar ../../pvesta/pvesta-client.jar -l ../../pvesta/serverlist -m test5-4.maude -f reduction.quatex -a 0.05 >> output5.txt

java -jar ../../pvesta/pvesta-client.jar -l ../../pvesta/serverlist -m test5-5.maude -f reduction.quatex -a 0.05 >> output5.txt

java -jar ../../pvesta/pvesta-client.jar -l ../../pvesta/serverlist -m test5-6.maude -f reduction.quatex -a 0.05 >> output5.txt

python do_read_p_res.py output5.txt





