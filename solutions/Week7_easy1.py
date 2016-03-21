# For Python 2.7

# Remove and return first node with given data from a singly linked list. 

import random 


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None  # Other Node


def linked_list_to_str(head):
    to_str = str(head.data)
    head = head.next
    while head is not None:
        to_str = to_str + "-->" + str(head.data)
        head = head.next
    return to_str


def make_shuffled_LL(start, end):
    head = None  # Used inside loop.
    prevNode = None  # Also used iside loop.
    options = list(range(start, end))
    for i in range(end):
        newNode = Node(random.choice(options))
        if i == 0:
    		head = newNode
                prevNode = newNode
        else:
        	prevNode.next = newNode
        	prevNode = newNode
    return head


def remove(head, element):
    current = head
    if current.data == element:
        head = current.next
        return current
    while current.next:
        if current.next.data == element:
      		temp = current.next
		current.next = current.next.next
 		return temp
	current = current.next
    return None


if __name__ == "__main__":
    head = make_shuffled_LL(0, 10)
    print "Linked list before removing node:", linked_list_to_str(head)
    print "Node that contains our element (6):", remove(head, 6)
    print "Linked list after removing node:", linked_list_to_str(head)
