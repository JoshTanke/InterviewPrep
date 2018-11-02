
# Searches a list and returns the index. Returns -1 if not in list.
# Complexity: O(log N)
def binary_search(arr, target):
	left, right = 0, len(arr)-1

	while left <= right:
		# discuss how you shouldn't do this outside python
		mid = (left + right) // 2

		if arr[mid] == target: return mid

		elif arr[mid] > target: right = mid - 1

		elif arr[mid] < target: left = mid + 1

	return -1

