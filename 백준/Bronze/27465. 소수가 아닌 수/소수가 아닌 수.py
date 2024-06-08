n = int(input())
if n == 1:
	n = 4
elif n > 1 and n < (10**8) * 5:
	n = n * 2
elif n > (10**8) * 5 and n % 2 != 0:
	n += 1
elif n > (10**8) * 5 and n % 2 == 0:
	pass
print(n)
