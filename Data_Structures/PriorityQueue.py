"""
Demoing a priority queue (python heapq)
A priority queue is used in 
	-- Dijkstra's
	-- Best First Search (A*)
	-- Minimum SPanning Tree (MST)
	-- Huffman coding

Time Complexities: 
	construction from list: O(n)
	removing root: O(logn)
	peeking root: O(1)
	adding: O(logn)

"""

from heapq import *

# Time Complexity: O(n logn)
# Space Complexity: O(1)
def heapsort(arr):
	heap = []
	for item in arr:
		heappush(heap, item)
	print(heap)
	return [heappop(heap) for _ in range(len(heap))]

a = [1, 5, 2, 3, 4]
print(heapsort(a))