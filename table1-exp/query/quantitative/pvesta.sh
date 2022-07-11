#!/usr/bin/bash
#
# Run PVesta
# Syntax: pvesta.sh <property name>
#

# Java command (recent versions of Java are not supported)
JAVA8_CMD="java"
# Extending the PATH may be needed for including the maude command
export PATH="$PATH:$(pwd)/tools_dir"

"$JAVA8_CMD" -jar pvesta-server.jar &
time "$JAVA8_CMD" -cp .:pvesta-client.jar vesta.Vesta -m ../test.maude -f "$1.quatex"

kill %1
