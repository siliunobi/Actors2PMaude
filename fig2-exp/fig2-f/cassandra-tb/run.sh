#!/bin/bash
host=`hostname -s`
test_file=test.maude

#metric="latency"
#metric="throughput"
#metric="readlatency"
#metric="gamma"
metric="gammaFreq"
#for loads in 180 100 ;
for loads in 180 ;
do
	for cls in 8 ;
	do
		for rlevel in "one" ;
		do
			conf="$metric-$loads-$cls-$rlevel"
			
			#metric_file="throughput.quatex"
      metric_file="gammaFreq.quatex"
			if [ $metric = 'latency' ];
			then
				metric_file="avglatency.quatex"
			fi

			echo $conf $metric_file

			python gen.py test.maude.temp1 test.maude $loads $cls $rlevel
			echo `date`
			java -jar ../../pvesta/pvesta-client.jar -l ../../pvesta/serverlist1 -m ${test_file} -f ${metric_file} -a 0.05 > ${host}-$conf.out 2>&1
			echo `date`
            result=`python result.py ${host}-$conf.out`
			echo $conf $result
			echo $conf $result >> result.out
		done
	done
done

for loads in 180 ;
do
	for cls in 8 ;
	do
		for rlevel in "one" ;
		do
			conf="$metric-$loads-$cls-$rlevel"
			
			#metric_file="throughput.quatex"
      metric_file="gammaFreq.quatex"
			if [ $metric = 'latency' ];
			then
				metric_file="avglatency.quatex"
			fi

			echo $conf $metric_file

			python gen.py test.maude.temp2 test.maude $loads $cls $rlevel
			echo `date`
			java -jar ../../pvesta/pvesta-client.jar -l ../../pvesta/serverlist1 -m ${test_file} -f ${metric_file} -a 0.05 > ${host}-$conf.out 2>&1
			echo `date`
            result=`python result.py ${host}-$conf.out`
			echo $conf $result
			echo $conf $result >> result.out
		done
	done
done

for loads in 180 ;
do
	for cls in 8 ;
	do
		for rlevel in "one" ;
		do
			conf="$metric-$loads-$cls-$rlevel"
			
			#metric_file="throughput.quatex"
      metric_file="gammaFreq.quatex"
			if [ $metric = 'latency' ];
			then
				metric_file="avglatency.quatex"
			fi

			echo $conf $metric_file

			python gen.py test.maude.temp3 test.maude $loads $cls $rlevel
			echo `date`
			java -jar ../../pvesta/pvesta-client.jar -l ../../pvesta/serverlist1 -m ${test_file} -f ${metric_file} -a 0.05 > ${host}-$conf.out 2>&1
			echo `date`
            result=`python result.py ${host}-$conf.out`
			echo $conf $result
			echo $conf $result >> result.out
		done
	done
done

for loads in 180 ;
do
	for cls in 8 ;
	do
		for rlevel in "one" ;
		do
			conf="$metric-$loads-$cls-$rlevel"
			
			#metric_file="throughput.quatex"
      metric_file="gammaFreq.quatex"
			if [ $metric = 'latency' ];
			then
				metric_file="avglatency.quatex"
			fi

			echo $conf $metric_file

			python gen.py test.maude.temp4 test.maude $loads $cls $rlevel
			echo `date`
			java -jar ../../pvesta/pvesta-client.jar -l ../../pvesta/serverlist1 -m ${test_file} -f ${metric_file} -a 0.05 > ${host}-$conf.out 2>&1
			echo `date`
            result=`python result.py ${host}-$conf.out`
			echo $conf $result
			echo $conf $result >> result.out
		done
	done
done

for loads in 180 ;
do
	for cls in 8 ;
	do
		for rlevel in "one" ;
		do
			conf="$metric-$loads-$cls-$rlevel"
			
			#metric_file="throughput.quatex"
      metric_file="gammaFreq.quatex"
			if [ $metric = 'latency' ];
			then
				metric_file="avglatency.quatex"
			fi

			echo $conf $metric_file

			python gen.py test.maude.temp5 test.maude $loads $cls $rlevel
			echo `date`
			java -jar ../../pvesta/pvesta-client.jar -l ../../pvesta/serverlist1 -m ${test_file} -f ${metric_file} -a 0.05 > ${host}-$conf.out 2>&1
			echo `date`
            result=`python result.py ${host}-$conf.out`
			echo $conf $result
			echo $conf $result >> result.out
		done
	done
done


for loads in 180 ;
do
	for cls in 8 ;
	do
		for rlevel in "one" ;
		do
			conf="$metric-$loads-$cls-$rlevel"
			
			#metric_file="throughput.quatex"
      metric_file="gammaFreq.quatex"
			if [ $metric = 'latency' ];
			then
				metric_file="avglatency.quatex"
			fi

			echo $conf $metric_file

			python gen.py test.maude.temp6 test.maude $loads $cls $rlevel
			echo `date`
			java -jar ../../pvesta/pvesta-client.jar -l ../../pvesta/serverlist1 -m ${test_file} -f ${metric_file} -a 0.05 > ${host}-$conf.out 2>&1
			echo `date`
            result=`python result.py ${host}-$conf.out`
			echo $conf $result
			echo $conf $result >> result.out
		done
	done
done

for loads in 180 ;
do
	for cls in 8 ;
	do
		for rlevel in "one" ;
		do
			conf="$metric-$loads-$cls-$rlevel"
			
			#metric_file="throughput.quatex"
      metric_file="gammaFreq.quatex"
			if [ $metric = 'latency' ];
			then
				metric_file="avglatency.quatex"
			fi

			echo $conf $metric_file

			python gen.py test.maude.temp7 test.maude $loads $cls $rlevel
			echo `date`
			java -jar ../../pvesta/pvesta-client.jar -l ../../pvesta/serverlist1 -m ${test_file} -f ${metric_file} -a 0.05 > ${host}-$conf.out 2>&1
			echo `date`
            result=`python result.py ${host}-$conf.out`
			echo $conf $result
			echo $conf $result >> result.out
		done
	done
done

for loads in 180 ;
do
	for cls in 8 ;
	do
		for rlevel in "one" ;
		do
			conf="$metric-$loads-$cls-$rlevel"
			
			#metric_file="throughput.quatex"
      metric_file="gammaFreq.quatex"
			if [ $metric = 'latency' ];
			then
				metric_file="avglatency.quatex"
			fi

			echo $conf $metric_file

			python gen.py test.maude.temp8 test.maude $loads $cls $rlevel
			echo `date`
			java -jar ../../pvesta/pvesta-client.jar -l ../../pvesta/serverlist1 -m ${test_file} -f ${metric_file} -a 0.05 > ${host}-$conf.out 2>&1
			echo `date`
            result=`python result.py ${host}-$conf.out`
			echo $conf $result
			echo $conf $result >> result.out
		done
	done
done




