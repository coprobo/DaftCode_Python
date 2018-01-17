# Piotr Walędzik

# Napisać kod tworzący listę list kolejnych elementów parzystych < 100 według
# schematu: [[0], [2], ... , [98]]. Wynikową listę przypisz na zmienną result.
lista = [[x] for x in range(0, 100, 2)]
print (lista)
#print(type(lista))

result = None
result = lista

assert result[1] == [2]