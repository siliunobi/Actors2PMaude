host=`hostname -s`

location=$1
cd ${location}
# replace PATH with the actual path
java -jar PATH/pvesta/pvesta-server.jar > server-${host}.out & 

