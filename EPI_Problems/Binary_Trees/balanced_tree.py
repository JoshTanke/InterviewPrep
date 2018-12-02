
class Node:

	def __init__(self, data=None):
		self.left = None
		self.right = None
		self.data = data


# post-order tree traversal
def helper(root):
	if not root: return -1
	
	left = helper(root.left) + 1
	right = helper(root.right) + 1

	if left == -1 or right == -1: return -1
	if abs(left-right) > 1: return -1

	return max(left, right)


# checks if a binary tree is balanced or not
# n nodes and height h => O(n) time and O(h) space
def check_height(root):

	if not root: return True

	return helper(root) != -1


"""
       n
     /   \
    n     n
   / \   / \
  n   n n   n
 / \         \
n   n         n
"""
root = Node()
root.left = Node()
root.left.left = Node()
root.left.left.left = Node()
root.left.left.left.left = Node()
root.left.left.left.right = Node()
root.left.right = Node()
root.right = Node()
root.right.right = Node()
root.right.left = Node()
root.right.right.right = Node()

print(check_height(root))

"""
       n
     /   \
    n     n
   / \     \
  n   n     n
 / \         \
n   n         n
"""
root = Node()
root.left = Node()
root.left.left = Node()
root.left.left.left = Node()
root.left.left.left.left = Node()
root.left.left.left.right = Node()
root.left.right = Node()
root.right = Node()
root.right.right = Node()
root.right.right.right = Node()

print(check_height(root))
