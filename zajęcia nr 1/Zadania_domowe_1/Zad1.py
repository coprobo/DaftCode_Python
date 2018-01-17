# Piotr Walędzik

# Stwórz listę liczb od 0 do 999.
# Liczby podzielne przez 3 zastąp słowem 'trzy'.
# Liczby podzielne przez 5 zastąp słowem 'pięć'.
# Liczby podzielne jednocześnie przez 3 i 5 zastąp słowem 'trzypięć'.
# Wynikową listę przypisz zmiennej result.

lista = [x for x in range(1000)]

for i in lista:
	if not i%5:
		lista[i] = 'pięć'
	if not i%3:
		lista[i] = 'trzy'
		if not i%5:
			lista[i] = 'trzypięć'

# print(lista)
# Wynikową listę przypisz zmiennej result.

result = None
result = lista
print(result)

assert result[15] == 'trzypięć'
