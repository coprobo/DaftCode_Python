# Piotr Walędzik

# Napisz kod transformujący podany słownik:
# {
#     1: 'Poniedziałek',
#     2: 'Wtorek',
#     3: 'Środa',
#     4: 'Czwartek',
#     5: 'Piątek',
#     6: 'Sobota',
#     7: 'Niedziela'
# }
# do postaci:
# {
#     'Poniedziałek': 1,
#     'Środa': 3,
#     'Piątek': 5,
#     'Niedziela': 7
# }
# (Zamiana klucza z wartością i zostawienie tylko dni nieparzystych).
# Wynik przypisz na zmienną result


tydzien = {
    1: 'Poniedziałek',
    2: 'Wtorek',
    3: 'Środa',
    4: 'Czwartek',
    5: 'Piątek',
    6: 'Sobota',
    7: 'Niedziela'
}

#print(type(tydzien[1]))
result = dict()

for i in range(1,8):
	if i%2:
		#print(tydzien[i])
		result.update({tydzien[i]:i})

print(result)
print(type(result))
assert 'Poniedziałek' in result
