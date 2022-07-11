import sys
import re
s=sys.argv[1]
lines = s.split("\n")
for line in lines:
    # path should be changed accordingly
	if "java -jar ../../pvesta/pvesta-server.jar" in line:
		print re.search(r'\d+', line).group()	
		

