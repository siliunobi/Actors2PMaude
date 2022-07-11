restartServer(){
	c=`ssh $1 "ps -ef | grep pvesta-server.jar"`
	num=`python getpid.py "$c"`
	echo "kill $num"
	ssh $1 "kill -9 $num"
}

# replace PATH with the actual path to the corresponding directory, e.g.,
# PATH=[path]/fig2-d, for running the experiments in Figure 2 (d)
# PATH=[path]/fig2-b/ramp_f_original_latency_msg, for running the experiments of RAMP-F in Figure 2 (b)
#
# Example path used in our experiments on Emulab:
# location=/users/nobi/pvesta/examples/pet/experiment/ramp_1pw
location=PATH

for node in `cat emulabnodes`
do
	echo "$node"
	nohup ssh $node "./server.sh" ${location}
done
