#!/bin/env python2.7

"""
Added by wendyjan on 2/8/2016.
For Python 2.7 
"""


class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


def linked_length(head):
    if not head:
        return 0
    count = 1
    temp = head
    while temp.next:
        count += 1
        temp = temp.next
    return count


if __name__ == "__main__":
    data = range(1, 13)  # Creates list of ints from 1 to 12.
    head = Node(data[0])
    temp = head
    for d in data[1:]:
        temp.next = Node(d)
        temp = temp.next
    print "The length of linked list with data", data, "is:", linked_length(head)
    head = head.next
    print "The length of linked list with data", data[1:], "is:", linked_length(head)


