# Zadanie 4
# Napisz funkcję factorial, która dla danego n obliczy rekurencyjnie silnię

#Piotr Walędzik

def factorial(n):
	if n<0:
		print('Nie ma silni z liczb mniejszych od zera')
	elif n == 0 or n==1:
		return 1
	else:
		return(n * factorial(n-1))

assert factorial(5) == 120