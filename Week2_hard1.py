"""
Added by wendyjan on 2/8/2016.
"""

from Week2_easy1 import is_palindrome


def make_palindrome(word):
    """
    Builds the shortest possible palindrome from the given word,
    by adding characters at the front or back of the word.
    """
    if len(word) < 2 or is_palindrome(word):
        return word
    i = len(word) -1
    while i > 0:
        if i != len(word) -1 and is_palindrome(word[i:]):
            return word + word[i-1::-1]
        if is_palindrome(word[0:i]):
            return word[:i - 1:-1] + word
        i -= 1
    

if __name__ == "__main__":
    test_cases = ["otto", "", "hi", "o", "hii", "iih", "haahfr", "frhaah", "haifriend"]
    for t in test_cases:
        print t, ":", make_palindrome(t)
