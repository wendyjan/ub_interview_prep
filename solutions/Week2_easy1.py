#!/bin/env python2.7

"""
Added by wendyjan on 2/8/2016.
For Python 2.7 
"""


def is_palindrome(word):
    tail_index = len(word) - 1
    head_index = 0
    while tail_index > head_index:
        if word[tail_index] != word[head_index]:
            return False
        else:
            tail_index -= 1
            head_index += 1
    return True

# Alternate solution:
# def is_palindrome(word):
#     return word == word[::-1]

if __name__ == "__main__":
    test_cases = ["otto", "otsto", "", "hi", "o", "ots2o"]
    for t in test_cases:
        print t, ":", is_palindrome(t)
