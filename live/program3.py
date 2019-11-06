# # This is a Python Demo - List

# Declare and Display a List
L = ['red', 'green', 'blue', 'yellow', 'black']
print(L[0])		# red
print(L[2])		# blue

# Slicing a Elements from List
M = ['a', 'b', 'c', 'd', 'e', 'f']
print(M[2:5])		# ['c', 'd', 'e']
print(M[0:2])		# ['a', 'b']
print(M[3:-1])		# ['d', 'e']

# CHANGING A ELEMENT OF LITS
N = ['red', 'green', 'blue']
N[0] = 'orange'
print(N)    # ['orange', 'green', 'blue']
N[-1] = 'violet'
print(N)    # ['orange', 'green', 'violet']

# ADDING A ELEMENT OF LITS
O = ['red', 'green', 'yellow']
O.append('blue')
print(O)    # ['red', 'green', 'yellow', 'blue']