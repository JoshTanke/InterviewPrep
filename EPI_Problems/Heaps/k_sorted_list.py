from heapq import *


# sort a list whose elements are at most k distance from correct location
# n items => O(nlogk) time O(k) space
def k_sorted_list(li, k):

	heap = li[:k]
	heapify(heap)

	return_li = []

	for item in li[k:]:
		return_li.append(heappushpop(heap, item))

	while heap:
		return_li.append(heappop(heap))

	return return_li


li = [3, -1, 2, 6, 4, 5, 8]
sorted_li = k_sorted_list(li, 2)
print(sorted_li)