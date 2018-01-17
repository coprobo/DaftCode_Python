# Funkcje - 31.10.2017

'''def choinka(znak):
    for i in range(4):
        k = i*" "
        print((4-i)*k + i*"{}".format(znak))

def draw3():
	for drawing in range(3):
		choinka('*')'''


#Domyslny argument w funkcji po prostu cos przypisujemy, jak nizej "sign=*"
def draw_tree(h, sign='*'):
	symbols_count = 0
	for i in range(h):
		symbols_count += (2 * i + 1) #zliczam uzyte symbole
		print((h-i-1) * ' ' + (2 * i + 1) * '{}'.format(sign))
	return symbols_count

print('Podaj h, większe od 3 =')
h = input()
h = int(h)

print('Czy chcesz rysowac czyms innym niz *? \n TAK/NIE')
choice = input()
if choice == 'TAK':
	print('Podaj znak do rysowania:')
	sign = input()
else:
	sign = '*'

print('\n \n \n')

for i in range(h):
	symbols = draw_tree(i, sign)
	print(symbols) #wypisuje ilosc symboli uzytych

#Zasięg widoczności:
#przestrzenie nazw, kazda zmienna jesli zostala zaimplementowana pod funkcja to jest inna zmienna niz ta zaimplementowana globlnie lub pod jeszcze inna funkcja
# mimo to ze moga miec te same nazwy (te zmienne)



