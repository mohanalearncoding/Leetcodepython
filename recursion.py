# Assume that n is greater than or equal to 1 */
def fun1(n):
	if(n == 1):
		return 0
	else:
		return 1 + fun1(n/2)

print(fun1(8))
