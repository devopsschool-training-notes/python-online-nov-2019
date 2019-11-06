x = 6
while x:
    print(x)
    x -= 1
    if x == 3:
        break
# 6 5 4


x = 6
while x:
	x -= 1
	if x % 2 != 0:
		continue
	print(x)
# 4 2 0