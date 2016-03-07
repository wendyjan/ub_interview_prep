import collections

class Node:

	def __init__(self, d, name):
		self.data = d
		self.name = name 
		self.left = None
		self.right = None

class Contestant_Tree:

	def __init__(self):
		self.rep_scores = range(14)
		self.names = ["Ashley", "Wendy", "Ziyun", "Nina",
                              "Tyler", "Taylor", "Noah", "Naomi",
			      "Jeff", "Adam", "Sara", "Reese",
			      "Joan", "Zach"]
		self.root = self.make_bst(0, len(self.rep_scores) - 1)

	def make_bst(self, start, end):
		if end < start:
			return None
		mid = (start + end) / 2
		root = Node(self.rep_scores[mid], self.names[mid])
		root.left = self.make_bst(start, mid - 1)
		root.right = self.make_bst(mid + 1, end)
		return root


def traverse_postorder(root, data_list):
	if root:
		traverse_postorder(root.right, data_list)
		data_list.append(root)
                traverse_postorder(root.left, data_list)


def make_team(root, team_num):	
 	data = []
 	traverse_postorder(root, data)
	team = []
	for i, d in enumerate(data):
		if i % 4 == team_num:
			team.append(d.name)
	return team

if __name__ == "__main__":
	x = range(20)
	root = Contestant_Tree().root
	print root.data
	print root.name
	print make_team(root, 0)

