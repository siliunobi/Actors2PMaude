#!/bin/sh
#
# Script for running the quantitative analysis
#
# We assume the following is installed:
#  - Python 3.7 or above,
#  - umaudemc (pip install umaudemc, its command should be in the path),
#  - LTSmin (its commands should be in the path or LTSMIN_PATH be set appropriately),
#  - the Maude plugin for LTSmin (whose path should be set with MAUDEMC_PATH),
#  - psutil (pip install psutil, for memory measurement),
#  - the Spot Python library,
#

export MAUDEMC_PATH="$(pwd)/tools_dir/libmaudemc.so"	# change to .dylib for macOS
export NUSMV_PATH="$(pwd)/tools_dir/bin"
export LTSMIN_PATH="$(pwd)/tools_dir/bin"

# Benchmark the examples with Maude, LTSmin, and Spot
python -m umaudemc test testCases.yaml --benchmark --backend maude,ltsmin,spot --repeats 3

# Measure memory consumption for the same examples
python -m umaudemc test testCases.yaml --memory --backend maude,ltsmin,spot --memory-method psutil

