#!/usr/bin/env python3
#
# Simple memory usage measurement script based on psutil
#

import sys
import time
import psutil

# Peak of heap memory usage
max_heap = 0.0

try:
	# Forward the arguments as a command invocation
	with psutil.Popen(sys.argv[1:]) as p:

		# Measures memory usage twice a second
		while p.is_running() and p.status() != psutil.STATUS_ZOMBIE:
			time.sleep(0.5)

			heap = p.memory_info().rss
			# Child processes are also included in the count
			for child in p.children(recursive=True):
				heap += child.memory_info().rss

			if heap > max_heap:
				max_heap = heap

		p.wait()
		print(f'Memory peak: {max_heap}', file=sys.stderr)

except Exception as e:
	print(e)
	print(f'Memory peak: {max_heap}', file=sys.stderr)
