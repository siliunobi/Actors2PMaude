c=`ssh $1 "ps -ef | grep pvesta-server.jar"`
num=`python getpid.py "$c"`
echo "kill $num"
ssh $1 "kill -9 $num"
