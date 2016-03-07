#!/bin/env python2.7

"""
Added by wendyjan on 3/7/2016.
For Python 2.7 
"""

def count_occurrences(a, b):
	count = 0
	for i in range(len(b) - len(a) + 1):
		if a ==  b[i: i + len(a)]:
			count += 1
	return count


if __name__ == "__main__":
	print count_occurrences('xx', 'xxxx')



