"""
For Python 2.7

See document at https://docs.google.com/document/d/1Mmu5y-72pQ_z2-KHqK1kxc5WQ3zCn1--nFAjn0d0cck/edit?usp=sharing, 
and http://www.tutorialspoint.com/python/bitwise_operators_example.htm.
"""


def is_even(b):
	return not bool(int(b, 2) & 1)


if __name__ == "__main__":
	b = '0b00001100'
	print is_even(b)
	b = '0b00111001'
	print is_even(b)
