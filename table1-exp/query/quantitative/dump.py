#!/usr/bin/env python3
#
# Dump execution traces of PMaude models for MC2
#

import sys
from itertools import chain

import maude


def simulate(current, getTime, tick, length, observations):
	"""Obtain a single execution of the PMaude model"""

	print('0.0 0.0')

	current = tick(current)
	current.rewrite()

	time = getTime(current)
	time.reduce()

	values = [obs(current) for obs in observations]

	for value in values:
		value.reduce()

	print(*map(str, chain((time,), values)))

	current = tick(current)
	current.rewrite()


def main():
	import argparse

	parser = argparse.ArgumentParser(description='Dump PMaude execution traces')

	parser.add_argument('--size', '-s', help='Size of the sample (number of executions)', type=int, default=30)
	parser.add_argument('--length', '-l', help='Maximum length of every execution', type=int, default=100)
	parser.add_argument('--seed', '-r', help='Random seed', type=int, default=0)
	parser.add_argument('source', help='Maude source file')
	parser.add_argument('observation', help='Observations', nargs='*')

	args = parser.parse_args()

	maude.init()
	maude.setRandomSeed(args.seed)

	maude.load(args.source)

	m = maude.getCurrentModule()
	t = m.parseTerm('initState')

	if not t:
		print('Error: the initial state "initState" is not defined.', file=sys.stderr)
		return 1

	config_kind = m.findSort('Config')

	if not config_kind:
		print('Error: the "Config" of PMaude configurations is not defined.', file=sys.stderr)
		return 1

	config_kind = config_kind.kind()

	float_kind = m.findSort('Float').kind()

	getTime = m.findSymbol('getTime', (config_kind, ), float_kind)

	if not getTime:
		print('Error: the "getTime" function is not defined.', file=sys.stderr)
		return 1

	tick = m.findSymbol('tick', (config_kind, ), config_kind)

	if not tick:
		print('Error: the "tick" function is not defined.', file=sys.stderr)
		return 1

	observations = []

	for obs_text in args.observation:
		obs = m.findSymbol(obs_text, (config_kind, ), float_kind)

		if not obs:
			print(f'Error: cannot find observation function "{obs_text}".')
			return 1

		observations.append(obs)

	header = ' '.join(chain('T', args.observation))

	t.rewrite()

	for _ in range(args.size):
		print(header)
		simulate(t.copy(), getTime, tick, args.length, observations)
		print()


if __name__ == '__main__':
	sys.exit(main())
