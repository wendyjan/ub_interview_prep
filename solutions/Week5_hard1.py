# For Python 2.7
"""
Given a tree and element e, return a list of which levels of the tree contain e.

Note that if e occurs several times on level x, 
then level x will be included that many times in the return array.
"""

import collections

class Node:

    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
	self.children = []
        self.visited = False

def get_containing_levels(root, e):
    if root is None:
        return []
    q = collections.deque()
    q.append(root)
    levels_with_e = []
    level_counter = -1
    while len(q) > 0:
        level_counter += 1
        for i in range(len(q)):
            temp_node = q.popleft()
            if temp_node.data == e:
	        levels_with_e.append(level_counter)
            for child in temp_node.children:
                    q.append(child)
    return levels_with_e 


if __name__ == "__main__":
    root = Node(5)
    for i in range(3):
        root.children.append(Node(i))
    for child in root.children:
 	for j in range(3):
            child.children.append(Node(j))
    print (get_containing_levels(root, 2))

