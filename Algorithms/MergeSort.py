

def merge(a, b):
	merged_array = []
	min_len = min(len(a), len(b))

	i = j = 0
	while i < len(a) and j < len(b):
		if a[i] <= b[j]:
			merged_array.append(a[i])
			i += 1
		else:
			merged_array.append(b[j])
			j += 1

	if i < len(a):
		merged_array.extend(a[i:])
	if j < len(b):
		merged_array.extend(b[j:])

	return merged_array


def mergeSort(a):

	if len(a) <= 1: return a 

	mid = len(a) // 2
	left, right = a[:mid], a[mid:]
	
	left = mergeSort(left)
	right = mergeSort(right)
	result = merge(left, right)
	print(left, right)
	print(result)
	print('')
	# print(result)

	return result




arr = [5, 2, 8, 1, 9, 7, 6, 3, 4]
print(mergeSort(arr))