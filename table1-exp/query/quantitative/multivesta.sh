#!/usr/bin/bash
#
# Run MultiVeSta
# Syntax: multivesta.sh <property name>
#

# Java command (any version of Java is apparently supported)
JAVA8_CMD="java"
# Extending the PATH may be needed for including the maude command
export PATH="$PATH:$(pwd)/tools_dir"

time "$JAVA8_CMD" -jar multivesta.jar -c -sd vesta.pmaude.NewAPMaudeState -o "-mc maude" -l 1 -m ../test.maude -f "$1.multiquatex" -vp false -verboseServers false
