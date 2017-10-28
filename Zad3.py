# Piotr Walędzik

# Stwórz listę 100 list, każda z liczbami od 1 do 100. Potem dla każdej j-tej
# z tych list wewnętrznych na jej końcu dodać sumę jej pierwszych elementów
# do j-tego włącznie.
# Spodziewany efekt: [ [1, 2, 3, ..., 100, 1], [1, 2, 3, ..., 100, 3],
# [1, 2, 3, ..., 100, 6], ..., [1, 2, 3, ..., 100, 5050] ]
# Wynikową listę przypisz na zmienną result

lista100 = []
for i in range(100):
    lista = [x for x in range(1, 101)]
    lista100.append(lista)
    lista100[i].append(sum(lista100[i][0:i+1]))


print(lista100)

result = None
result = lista100

assert result[-1][-1] == 5050