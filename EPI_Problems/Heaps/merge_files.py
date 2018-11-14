from heapq import *

# merges k files of length n in O(nlogk) time using O(k) space (excluding return list)
# assuming files are of same length and don't come pre-sorted
def merge_files(files):

	files = [sorted(f, reverse=True) for f in files]

	return_li, heap = [], []

	for i,f in enumerate(files): heappush(heap, (f.pop(), i))

	while heap:
		item, index = heappop(heap)
		return_li.append(item)
		
		if files[index]:
			new_item = files[index].pop()
			heappush(heap, (new_item, index))

	return return_li



files = [ [6,2,7,1], [3,1,4,8], [5,4,8,9] ]

merged_files = merge_files(files)
print(merged_files)
