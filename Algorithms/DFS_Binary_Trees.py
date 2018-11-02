"""
All traversals below are forms of DFS.

Node Class

class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None


Example Tree:

		d
	   / \
	  b	  e
	 / \   \
	a   c	f
"""

# D, B, A, C, E, F
# Complexity: O(n) time, O(h) space
def pre_order_traversal(root):
	if root == None: return

	print(root.val)
	pre_order_traversal(root.left)
	pre_order_traversal(root.right)


# A, C, B, F, E, D
# Complexity: O(n) time, O(h) space
def post_order_traversal(root):
	if root == None: return

	post_order_traversal(root.left)
	post_order_traversal(root.right)
	print(root.val)


# A, B, C, D, E, F
# Complexity: O(n) time, O(h) space
def in_order_traversal(root):
	if root == None: return

	in_order_traversal(root.left)
	print(root.val)
	in_order_traversal(root.right)
