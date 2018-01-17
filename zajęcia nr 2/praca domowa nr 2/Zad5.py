# Zadanie 5
# Napisz funkcję function_results_sum, która przyjmuje dowolną liczbę funkcji
# jako argumenty pozycyjne.
# Argumenty do poszczególnych funkcji przekazywane są do function_results_sum jako keyword arguments w
# postaci NAZWA_FUNKCJI=ARGUMENTY.
# Funkcja function_results_sum powinna zwrócić sumę wyników otrzymanych 
# po odpaleniu każdej z funkcji z odpowiednimi argumentami.
# Jeżeli funkcja jest bezargumentowa, nie oczekuje się podania do niej
# argumentów
# Gdy funkcja przyjmuje jeden argument, jako keyword argument przekazany 
# będzie int, np. one_arg_function_name=2
# Gdy funkcja przyjmuje więcej argumentów - oczekiwana jest tupla odpowiedniej
# długości, np. two_args_function_name=(1, 2)

# przykład 1:
# sygnatury funkcji:
# def no_arg()
# def one_arg(a)
# def multiple_args(a, b, c, e, f)
#
# wywołanie function_results_sum:
# function_results_sum(
#     no_arg, one_arg, multiple_args,
#     one_arg=23,
#     multiple_args=(1, 2, 3, 4, 5)
# )

# inne wywołanie function_results_sum:
# function_results_sum(
#     no_arg, one_arg, multiple_args,
#     one_arg=-1245,
#     multiple_args=(45, 65, 76, 123456, 111.222)
# )
# 
# W zadaniu skorzystaj z atrybutu __name__ dostępnego na obiekcie funkcji
#
# Zadanie nie wymaga sprawdzania poprawności przekazywanych argumentów,
# obowiązek przekazania odpowiedniej liczby argumentów do wszystkich funkcji spoczywa na tym, kto wywołuje function_results_sum
#
# Do odpowiedniego uruchomienia funkcji przyda się operator * przy wywołaniu funkcji. Poniżej przydatne linki:
# https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists
# https://stackoverflow.com/questions/2921847/what-does-the-star-operator-mean

#Piotr Walędzik

def no_arg():
    return 5

def ident(x):
    return x

def mult(x, y):
    return x * y

def multiple_args(a, b, c, d ,e):
	return a*b*c*d*e

def function_results_sum(*args, **kwargs):
	#ustawiam zmienna na 0 do sumowania
    suma = 0
    #iteruje po ilosci funkcji w args
    for func in args:
    	#printuje jaka mam aktualnie funkcje w danej iteracji
    	print(func.__name__)

    	#Warunki zeby podawac int z funkcji, rozpakowywac tuple i podawac to co jest pod funkcją no_arg
    	if func.__name__ in kwargs: #Jesli istnieje taka nazwa funkcji jak key word argument, do jakiego cos przypisujemy w naszych kwargs
    		if type(kwargs[func.__name__]) == int: #Jesli podajemy int jako argument funkcji
    			suma += func(kwargs[func.__name__]) #to wykonujemy te funkcje bezposrednio od int
    		elif type(kwargs[func.__name__]) == tuple: #Jesli podajemy tuple jako argument funkcji
    			suma += func(*kwargs[func.__name__]) #to musimy ja rozpakowac, zeby byla szeregiem argumentow do naszej funkcji
    	else: # w przeciwnym razie nic nie podajemy do funkcji, czyli zwraca tylko to co ma w sobie
    		suma += func()
    return suma #zwracam sume returnów naszych funkcji


#function_results_sum(no_arg, ident, mult, multiple_args, ident=2, mult=(3, 4), multiple_args=(1, -2, 3, -4, 5.154))

#result = function_results_sum(no_arg, ident, mult, multiple_args, ident=2, mult=(3, 4), multiple_args=(1, -2, 3, -4, 5.154))
#print(result)


assert function_results_sum(no_arg, ident, mult, ident=2, mult=(3, 4)) == 19