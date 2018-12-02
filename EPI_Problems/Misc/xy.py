
import math

def x_to_y(x, y, d):
	if y == 1 or x == 1: return x
	if y == 0: return 1
	if y in d: return d[y]

	d[y] = x_to_y(x, y//2, d) * x_to_y(x, math.ceil(y/2), d)
	return d[y]


print(x_to_y(3, 9, {}))