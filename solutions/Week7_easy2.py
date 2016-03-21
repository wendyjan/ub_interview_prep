# For Python 2.7

# Convert a character "phone number".  For example, "CALLUSA" would be 225-5872.


def convert_to_digits(s):
	s = s.lower()  # We will use lowercase ASCII values of chars.
        digits = []
	char_values = [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9]
	for i in range(len(s)):
                if i == 3:
			digits.append("-")
		char_i = ord(s[i]) - 97  # This method gives the int value of this char in ASCII.
		digits.append(str(char_values[char_i]))
	return "".join(digits)


if __name__ == "__main__":
	print convert_to_digits("CALLUSA") 

