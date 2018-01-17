# Zadanie 6
# Jesteś administratorem Bardzo Wysokiego Budynku Biurowego BWBB.
# Masz listę ile osób znajduje się na kolejnych piętrach BWBB: `lista_osob` (czyli wartość lista_osób[5] to liczba osób na piętrze nr 5) - zawiera ona 
# tylko liczby całkowite
# W budynku znajduje się określona liczba ewakuacyjnych klatek schodowych: `liczba_klatek_schodowych` - jest to liczba całkowita
# Każda z klatek pozwala na jednoczesne poruszanie się kilku osób obok siebie: `liczba_osob_w_rzedzie` (liczba całkowita).
# Odstęp czasowy miedzy każdym ewakuowanym rzędem osób to 1 sekunda.
# `tempo_schodzenia` to liczba sekund potrzebna na przejście jednego piętra. Uznajemy, że wszyscy schodzą w tym samym tempie
# Ewakuacja budynku zaczyna się od najwyższego piętra, piętro po piętrze w dół.
# Po jakim czasie powinna zaczynać się ewakuacja dla poszczególnych pięter żeby nie tworzyły się zatory?
# Zatory nie tworzą się wtedy, gdy osoby z wyższych minęły już piętro, które jest w danym momencie ewakuowane. 
# Funkcja ewakuacja powinna zwracać listę z intami po ilu sekundach od rozpoczęcia ewakuacji budynku  na każdym piętrze zostanie włączony alarm 
# czyli result[6] przechowuje po ilu sekundach został włączony alarm na szóstym piętrze


# Osoby ewakuowane same rozkładają się po równo na liczbę zejść ewakuacyjnych
# Piętro zaczyna się ewakuować od razu po uruchomieniu na nim alarmu
# Argumenty do funkcji będą przekazane po nazwie, jako keyword

def ewakuacja(lista_osob, liczba_klatek_schodowych, liczba_osob_w_rzedzie, tempo_schodzenia):
	time = [0]
	liczba_pieter = len(lista_osob)
	time = liczba_pieter * time
	temp = 0
	#print(time)

	for i in range(1, liczba_pieter+1):
		#print(lista_osob[-i])

		ilosc_grup = lista_osob[-i]/liczba_osob_w_rzedzie
		reszta_z_grup = lista_osob[-i]%liczba_osob_w_rzedzie
		#print(ilosc_grup)
		if reszta_z_grup == 0:
			ilosc_grup = int(ilosc_grup)
			#print(ilosc_grup)


		else:
			ilosc_grup = int(ilosc_grup) + 1
			#print(ilosc_grup)

		#to moge zapakowac w funkcje ilosc_wypuszczen(argumenty)
		ilosc_wypuszczen = ilosc_grup / liczba_klatek_schodowych
		if ilosc_grup%liczba_klatek_schodowych == 0:
			ilosc_wypuszczen = int(ilosc_wypuszczen)
			#print(ilosc_wypuszczen)
		else:
			ilosc_wypuszczen = int(ilosc_wypuszczen) + 1
			#print(ilosc_wypuszczen)

		# time[-(i+1)] = czas zejscia + [(ilosc wypuszczen -1 ) * 1 <--- czas na przerwy miedzy grupami] +
		# + 1s (bo jak grupa mija pietro to kolejna czeka 1s jeszcze) ===> alarm na pietrze nizej
		# te sekundy -1 i +1 sie znoszą -> time = tempo_schodzenia + ilosc wypuszczen
		#time[i] = tempo_schodzenia + (ilosc_wypuszczen)
		#print(time)

		#temp += tempo_schodzenia + ilosc_wypuszczen
		#print(temp)
		if i == 1:
			time[-i] = temp
			temp += tempo_schodzenia + ilosc_wypuszczen
		else:
			time[-i] = temp
			temp += tempo_schodzenia + ilosc_wypuszczen
			#time[-i] = tempo_schodzenia + ilosc_wypuszczen
		# print(tempo_schodzenia + ilosc_wypuszczen)
		print(time)
	return time


# lista_osob = [5, 10, 15, 24, 2043, 187, 44]
# liczba_klatek_schodowych = 7
# liczba_osob_w_rzedzie = 3
# tempo_schodzenia = 10

# ewakuacja(
# 	lista_osob=lista_osob,
#     liczba_klatek_schodowych=liczba_klatek_schodowych,
#     liczba_osob_w_rzedzie=liczba_osob_w_rzedzie,
#     tempo_schodzenia=tempo_schodzenia
#  )



lista_osob = [5, 10, 15]
liczba_klatek_schodowych = 2
liczba_osob_w_rzedzie = 1
tempo_schodzenia = 30

assert [73, 38, 0] == ewakuacja(
    lista_osob=lista_osob,
    liczba_klatek_schodowych=liczba_klatek_schodowych,
    liczba_osob_w_rzedzie=liczba_osob_w_rzedzie,
    tempo_schodzenia=tempo_schodzenia
)