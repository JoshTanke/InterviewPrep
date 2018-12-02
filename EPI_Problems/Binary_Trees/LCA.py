
class Node:

	def __init__(self, data=None):
		self.left = None
		self.right = None
		self.data = data



def LCA(root, a, b):

	if not root: return 0, None
	
	if root.data == a or root.data == b: return 1, root
	
	leftNum, leftNode = LCA(root.left, a, b)
	rightNum, rightNode = LCA(root.right, a, b)

	if leftNum == 2: return leftNum, leftNode
	if rightNum == 2: return rightNum, rightNode

	if leftNum + rightNum == 2: return 2, root

	if leftNum >= rightNum: return leftNum, leftNode
	return rightNum, rightNode

"""
       a
     /   \
    b     c
   / \   / \
  d   e f   g
 / \         \
h   i         j
"""
root = Node('a')
root.left = Node('b')
root.left.left = Node('d')
root.left.left.left = Node('h')
root.left.left.right = Node('i')
root.left.right = Node('e')
root.right = Node('c')
root.right.right = Node('g')
root.right.left = Node('f')
root.right.right.right = Node('j')

print(LCA(root, 'f', 'i')[1].data) #a
print(LCA(root, 'f', 'j')[1].data) #c
print(LCA(root, 'e', 'i')[1].data) #b
print(LCA(root, 'h', 'i')[1].data) #d