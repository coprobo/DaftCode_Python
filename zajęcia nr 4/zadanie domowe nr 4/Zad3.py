# Chcemy napisać kod, który dla danego pliku z listą stolic wygeneruje number_of_sets zestawów pytań po number_of_questions_per_set pytań
# - Format listy stolic taki jak w stolice.csv
# - Format oczekiwanego pojedynczego zestawu pytań taki jak w pliku pytania.csv - prosimy pamiętać o nagłówkach
# - Każdy zestaw powinien znaleźć się w osobnym pliku - pierwszy w zestaw1.csv, drugi w zestaw2.csv itd (nie ma czegoś takiego jak zestaw 0)
# - pliki zestaw1.csv, zestaw2.csv itd. powinny się stworzyć w folderze z rozwiązaniem zadania (tzn. przy otwieraniu pliku nie podawać żadnej ścieżki, tylko samą nazwę pliku)
#
# Dodatkowe założenia:
# Pytanie o jeden kraj nie może wystąpić więcej niż raz (biorąc pod uwagę wszystkie zestawy)
# W przypadku, gdy ktoś poda nam dane, dla których musielibyśmy wygenerować więcej niż 48 pytań (tyle mamy stolic w pliku stolice.csv) - rzućmy ValueError
# Poprawna odpowiedź powinna znajdować się w losowej kolumnie - tzn. losowo powinna być odpowiedzią A, B, C lub D
# Do losowania należy skorzystać z modułu random https://docs.python.org/3/library/random.html

import random
import csv


def create_sets_of_question(capitals_csv, number_of_sets, number_of_questions_per_set):
    
    #tu powinienem miec zmiast 48 dlugosc pliku ze stolicami 
    if number_of_sets*number_of_questions_per_set > 48:
        #podnosze error
        raise ValueError

    with open(capitals_csv, 'r') as stolice:
        reader_capitals = csv.reader(stolice, delimiter=';')

        next(reader_capitals)
        capitals = []

        #wczytuje stolice
        for row in reader_capitals:
            capitals.append(row)
        #print(capitals)

        j = 0

        for i in range(1, number_of_sets + 1):
            file_name = 'zestaw{}.csv'.format(i)
            #print(file_name)
            with open(file_name, 'w') as exam:
                #zestaw musi zaczynac sie od tej linijki
                exam.write('Państwo;A;B;C;D\n')
                for k in range(number_of_questions_per_set):
                    #iterujac dodaje pytanie

                    #randomowo wstawiam poprawna odpowiedz
                    place = random.randint(1,4)
                    print('iteracja po k nr: {}'.format(k))
                    print('miejsce na randomowa odpowiedz: {}'.format(place))

                    num1 = random.randint(1,47)
                    num2 = random.randint(1,47)
                    num3 = random.randint(1,47)
                    

                    #wykluczam zeby w odpowiedziach ie bylo duplikatow
                    if num1 == num2:
                        num2 = random.randint(1,47)
                    elif num1 == num3:
                        num3 = random.randint(1,47)
                    elif num2 == num3:
                        num3 = random.randint(1,47)

                    print('num1: {}'.format(num1))
                    print('num2: {}'.format(num2))
                    print('num3: {}'.format(num3))


                    if place == 1:
                        a = capitals[j][1]                        
                        exam.write('{};{};{};{};{}\n'.format(capitals[j][0], a, capitals[num1][1], capitals[num2][1], capitals[num3][1]))
                    elif place == 2:
                        a = capitals[j][1]
                        exam.write('{};{};{};{};{}\n'.format(capitals[j][0], capitals[num1][1], a, capitals[num2][1], capitals[num3][1]))
                    elif place == 3:
                        a = capitals[j][1]
                        exam.write('{};{};{};{};{}\n'.format(capitals[j][0], capitals[num1][1], capitals[num2][1], a, capitals[num3][1]))
                    elif place == 4:
                        a = capitals[j][1]
                        exam.write('{};{};{};{};{}\n'.format(capitals[j][0], capitals[num1][1], capitals[num2][1], capitals[num3][1], a))

                    j=j+1

            j = j + 1
            print(j)



create_sets_of_question('stolice.csv', 1, 8)