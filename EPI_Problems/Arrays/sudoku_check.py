import math

# checks if a partially_completed sudoku board is valid
# nxn array => O(n^2) time and O(n) space
def check_board(board):

	def has_duplicate(region):
		region = list(filter(lambda x: x != 0, region))
		return len(region) != len(set(region))

	n = len(board)

	for i in range(n):
		if has_duplicate([board[i][j] for j in range(n)]): return False
		if has_duplicate([board[j][i] for j in range(n)]): return False

	region_size = int(math.sqrt(n))

	for i in range(region_size):
		for j in range(region_size):
			if has_duplicate([board[a][b] for a in range(i*region_size, (i+1)*region_size) for b in range(j*region_size, (j+1)*region_size)]):
				return False

	return True


valid_board = [
				[5,3,0,0,7,0,0,0,0],
				[6,0,0,1,9,5,0,0,0],
				[0,9,8,0,0,0,0,6,0],
				[8,0,0,0,6,0,0,0,3],
				[4,0,0,8,0,3,0,0,1],
				[7,0,0,0,2,0,0,0,6],
				[0,6,0,0,0,0,2,8,0],
				[0,0,0,4,1,9,0,0,5],
				[0,0,0,0,8,0,0,7,9]	
			  ]

invalid_board = [
				[5,3,0,0,7,0,0,0,0],
				[6,0,0,1,9,5,0,0,0],
				[0,9,8,0,0,0,0,6,0],
				[8,0,0,0,6,0,0,0,3],
				[4,0,0,8,0,3,0,0,1],
				[7,0,0,0,2,0,0,0,6],
				[0,6,0,0,9,0,2,8,0],
				[0,0,0,4,1,9,0,0,5],
				[0,0,0,0,8,0,0,7,9]	
			  ]

print(check_board(valid_board))
print(check_board(invalid_board))




