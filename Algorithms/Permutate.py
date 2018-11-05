

def permutate(a, index):

	if len(a)-1 == index: print(a)

	for i in range(index, len(a)):
		a[index], a[i] = a[i], a[index]
		permutate(a, index+1)
		a[index], a[i] = a[i], a[index]

	return 

permutate([1, 2, 3, 4], 0)