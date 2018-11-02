

# complexity: O(n) time and O(h) space
# Graph Traversal
def iterative_DFS(node):
	stack = []
	stack.append(root)
	visited = {}

	while len(stack) > 0:
		node = stack.pop()
		if node not in visited:
			visited.add(node)
			for child in node.children:
				stack.append(child)

# Graph Traversal
def recursive_DFS(node, visited):
	visited.add(node)
	for child in node.children:
		if child not in visited:
			recursive_DFS(child, visited)


# Tree Traversal
def tree_DFS(root):
	stack = [root]

	while len(stack) > 0:
		node = stack.pop()
		visit(node)
		if node.right: stack.append(node.right)
		if node.left: stack.append(node.left)

