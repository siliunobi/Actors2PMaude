restartServer(){
    c=`ssh $1 "ps -ef | grep pvesta-server.jar"`
    num=`python getpid.py "$c"`
    echo "kill $num"
    ssh $1 "kill -9 $num"
}

for node in `cat emulabnodes`
do
    echo "$node"
    restartServer $node
#   nohup ssh $node "cd ~/pvesta/examples/$FOLDER; java -jar ~/pvesta/pvesta-server.jar > server-${node}.out &"
#   nohup ssh ${node} "sudo apt-get install screen"
#   for i in $c
#   do
#       nohup ssh ${node} "kill -9 $i" &
#   done
done