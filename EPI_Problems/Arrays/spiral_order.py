

# prints the spiral order of an array
# nxn array => O(n^2) time and O(n^2) space
def spiral_order(a):

	left = 0
	right = len(a) - 1

	res = []

	while left < right:
		for i in range(left, right): res.append(a[left][i])
		for i in range(left, right): res.append(a[i][right])
		for i in range(right, left, -1): res.append(a[right][i])
		for i in range(right, left, -1): res.append(a[i][left])

		left += 1
		right -= 1

	if left == right: res.append(a[right][right])

	return res


threeByThree = [ 
				[1,2,3], 
				[4,5,6], 
				[7,8,9] 
				]

fourByFour = [ 	
				[1,2,3,4], 
				[5,6,7,8], 
				[9,10,11,12], 
				[13,14,15,16] 
			]

print(spiral_order(threeByThree))
print(spiral_order(fourByFour))


