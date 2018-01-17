# przekazywaie dynamicznej ilosci argumentow do funckji
# 

#komentowanie calosci zaznaczonego kodu ctrl+shift+/
# def sum_numbers(*numbers):
# 	result = 0
# 	for x in numbers:
# 		result += x
# 	return result

# result = sum_numbers(1, 2, 3, 4)
# print(result)


#argumenty mozemy teraz nazywac, i potem do nich sie odwolywac w funkcji
#def print_kwargs(**kwargs):
# 	for k, v in kwargs.items():
# 		print(k)
# 		print(v)
	


# print_kwargs(k=1, a=3, e=5)

#kombinacja dwoch rzeczy

# def print_kwargs(*numbers, **kwargs):
# 	'''Ta funkcja jest przykladem 
# 	uzycia zmiennych'''
# 	result = 0
# 	for x in numbers:
# 		result += x
# 		print(result)

# 	for k, v in kwargs.items():
# 		print(k)
# 		print(v)

# 	return result

# print_kwargs(4, 5, 6, k=1, a=3, e=5)

# '''Jesli funkcja jest dokumentowana, to mozna sie dowiedziec co funkcja robi poprzez:'''
# print(print_kwargs.__doc__)


#############################################################

from Zajecia2 import draw_tree
draw_tree()