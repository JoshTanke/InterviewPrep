

def add_one(a):
	
	for i in range(len(a)-1, -1, -1):
		if a[i] + 1 > 9: 
			a[i] = 0
			if i == 0: 
				a[0] = 1
				a.append(0)
		else:	
			a[i] += 1
			break

	return a



print(add_one([0]))
print(add_one([9]))
print(add_one([1,9]))
print(add_one([1,9,9]))
print(add_one([9,9,9]))
print(add_one([3,9,1]))
