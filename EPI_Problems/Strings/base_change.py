import string


def to_int(num, base):
	is_neg = False
	res = 0
	for c in num:
		if c == '-': is_neg = True
		else: res = res * base + int(c)
	return res if not is_neg else -res

def int_to_base(num, base):
	if num == 0: return num
	is_neg = num < 0
	num = abs(num)
	res = []
	while num:
		ind = num % base
		res.append(string.hexdigits[ind].upper())
		num = num // base
	if is_neg: res.append('-')
	return ''.join(res[::-1])

# converts a num in baseOne to a num in baseTwo
# time complexity of num of length n: O(n*(1+log(baseTwo)baseOne))
def base_change(num, baseOne, baseTwo):
	decimal = to_int(num, baseOne)
	return int_to_base(decimal, baseTwo)

# 1A7
print(base_change('615', 7, 13))

# -1A7
print(base_change('-615', 7, 13))
	
