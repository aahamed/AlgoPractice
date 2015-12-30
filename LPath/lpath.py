"""
lpath.py: Given a binary tree compute the length of the longest path in the tree
where traversing an edge in a path results in an increment by 1.

Ex:

			5
		8		6
			  7	   12
				      13
					     14
						    15
							
	Ans = 4  path: (12, 13, 14, 15)
Author: Aadil Ahamed
"""

class Node(object):
	
	k = 1
	def __init__(self, value, left = None, right = None):
		self.value = value
		self.left = left
		self.right = right
		self.name = 'node' + str(Node.k)
		Node.k += 1
		
	def __str__(self):
		return self.name
		
	def childless(self):
		if self.left == None and self.right == None:
			return True
		else:
			return False
	
	def left_child(self):
		return self.left
		
	def right_child(self):
		return self.right

L = {}
def longest_frm(node):
	"""
		Longest incremental path beginning from node
	"""
	length_left = 0
	length_right = 0
	if node.childless():
		L[node] = 1
		return 1
	elif (node.left_child().value != node.value + 1) and (node.right_child().value != node.value + 1):
		L[node] = 1
		return 1
	if node.left_child() is not None and node.left_child().value == node.value + 1:
		length_left = longest_frm(node.left_child())
	if node.right_child() is not None and node.right_child().value == node.value + 1:
		length_right = longest_frm(node.right_child())
	max_length = max(length_left, length_right) + 1
	L[node] = max_length
	return max_length


def print_L():
	for key in L:
		print(key, L[key])

		
def test_longest_frm():
	node1 = Node(13)
	node2 = Node(7)
	node3 = Node(12, node1)
	node4 = Node(6, node2, node3)
	node5 = Node(11)
	node6 = Node(15)
	node7 = Node(10, node5)
	node8 = Node(9, node6, node7)
	node9 = Node(8, node8)
	root = Node(5, node9, node4)
	print(longest_frm(root))		# 3
	print(longest_frm(node1))		# 1
	print(longest_frm(node9))		# 4
	print(longest_frm(node4))		# 2
	print_L()


def main():
	test_longest_frm()
	
		
if __name__ == "__main__":
	main()
