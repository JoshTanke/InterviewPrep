

def partition(a, left, right, pivot):

	while left <= right:

		while a[left] < pivot: 
			left += 1
		while a[right] > pivot: 
			right -= 1
		
		if left <= right:
			a[left], a[right] = a[right], a[left]
			left += 1
			right -= 1

	return left

def quickSort(a, left, right):

	if left >= right: return 

	pivot_index = (left + right) // 2
	pivot = a[pivot_index]

	index = partition(a, left, right, pivot)
	quickSort(a, left, index - 1)
	quickSort(a, index, right)



a = [3, 2, 7, 1, 5, 9, 4, 8, 6]
quickSort(a, 0, len(a)-1)
print(a)