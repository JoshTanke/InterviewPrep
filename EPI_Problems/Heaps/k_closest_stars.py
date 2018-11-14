from heapq import *
import math


# helper function to calculate distance from earth
def compute_distance(star):
	x, y, z = star[0], star[1], star[2]
	return math.sqrt(x**2 + y**2 + z**2)

# calculate k closest stars to earth (0,0,0)
# n stars, k cloest => O(nlogk) time and O(k) space
def k_closest_stars(stars, k):

	stars = [(-compute_distance(star), star) for star in stars]

	heap = stars[:k]
	heapify(heap)

	for item in stars[k:]:
		heappushpop(heap, item)

	return [heappop(heap)[1] for _ in range(len(heap))]



stars = [ (1, 1, 1), (6, 2, 3), (1, 9, 1), (5, 3, 9), (2, 3, 1) ]
k_closest = k_closest_stars(stars, 3)
print(k_closest)


