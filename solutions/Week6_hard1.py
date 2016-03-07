"""
For Python 2.7

See document at https://docs.google.com/document/d/1andVX87rJrSvp7XFXCMWVevjkkErM_Y6cPlcBviAi14/edit?usp=sharing,
and http://www.tutorialspoint.com/python/bitwise_operators_example.htm.
"""


def larger_than_16(b):
	return bool(int(b, 2) & 240)


if __name__ == "__main__":
	b = '0b00001100'
	print larger_than_16(b)
	b = '0b00011100'
	print larger_than_16(b)
