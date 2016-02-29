#!/bin/env python2.7

"""
Added by wendyjan on 2/8/2016.
For Python 2.7 
"""


class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


def get_middle(head):
    if not head:
        return None 
    curr = head
    mid = head
    count = 0
    while curr.next:
        if count:
            mid = mid.next
            count = 0
        else:
            count = 1
        curr = curr.next
    return mid


if __name__ == "__main__":
    data = range(1, 13)  # Creates list of ints from 1 to 12.
    head = Node(data[0])
    temp = head
    for d in data[1:]:
        temp.next = Node(d)
        temp = temp.next
    middle = get_middle(head)
    print "The midpoint of list", data, "contains:", middle.val

