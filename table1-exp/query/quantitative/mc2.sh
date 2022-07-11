#!/usr/bin/bash
#
# Run MC2
# Syntax: mc2.sh <property name> <number of simulations>
#

# We imitate the random seeds of PVesta
if [ "$1" = "strong" ]; then
	seed=577625629
else
	seed=1669130500
fi

# Simulate the given number of executions
time python memusage.py python3 dump.py -s "$2" -r $seed -l 2 ../test.maude "$1" > "$1.traces"

# The last (optional) argument is the number of traces to be loaded into memory
# simultaneously, the greater the higher memory usage and the lower run time.
time python memusage.py java -jar MC2.jar stoch "$1.traces" "$1.query" 500
