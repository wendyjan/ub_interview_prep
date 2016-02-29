# For Python 2.7
"""
Given a sorted array of unique ints (ascending order), return a BST with minimal height.
"""

import collections


class Node:

    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None
        self.visited = False


def make_min_BST(int_list, start, end):
    if end < start:
        return
    mid = (start + end) / 2
    n = Node(data=int_list[mid])
    n.left = make_min_BST(int_list, start, mid - 1)
    n.right = make_min_BST(int_list, mid + 1, end)
    return n


def get_BST_levels(t):
    if t is None:
        return []
    q = collections.deque()
    q.append(t)
    all_levels = []
    while len(q) > 0:
        this_level = []
        for i in range(len(q)):
            temp_node = q.popleft()
            this_level.append(temp_node.data)
            for child in [temp_node.left, temp_node.right]:
                if child is not None:
                    q.append(child)
        all_levels.append(this_level)
    return all_levels


if __name__ == "__main__":
    int_list = range(1, 11)
    u = make_min_BST(int_list, 0, len(int_list) - 1)
    # Print the results to check them.
    for lev in get_BST_levels(u):
        print lev
