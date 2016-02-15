#!/bin/env python2.7

"""
Added by wendyjan on 2/15/2016.
For Python 2.7 
"""


def is_anagram(w1, w2):
    if len(w1) != len(w2):
        return False   # This isn't required for correctness.
    dict1 = {}
    dict2 = {}
    for c in w1:
        if c in dict1:
            dict1[c] += 1
        else:
            dict1[c] = 1
    for c in w2:
        if c in dict2:
            dict2[c] += 1
        else:
            dict2[c] = 1
    if dict1 == dict2: 
        return True
    else:
        return False


if __name__ == "__main__":
    test_cases = [("hello", "ellho"), ("", ""), ("Hello", "ellho")]
    for p1, p2 in test_cases:
        print p1, "and", p2, ":", is_anagram(p1, p2)


