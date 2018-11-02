from collections import deque


# Complexity:  O(n) time and O(n) space
def graph_BFS(root):

	visited = {}
	queue = deque(root)

	while queue:
		current = queue.popleft()

		if current.val = target: return True

		for child in current.children:
			if child not in visited:
				visited.add(child)
				queue.append(child)

	return False


# Complexity: O(n) time and O(n) space
def tree_BFS(root):

	queue = deque(root)

	while queue:
		current = queue.popleft()
		print(current.val)

		if current.left: queue.append(current.left)
		if current.right: queue.append(current.right)

