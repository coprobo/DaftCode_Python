# Chcemy napisać sprawdzarkę do testu znajomości stolic europejskich.
# Format listy stolic taki jak w pliku stolice.csv
# Format pytań taki jak w pliku pytania.csv
# Format odpowiedzi taki jak w pliku odpowiedzi.csv

# Napisz funkcję check_homework, która przyjmuje trzy argumenty:
# - capitals_csv to ścieżka do pliku, który zawiera listę stolic europejskich
# - questions_csv to ścieżka pliku csv, który zawiera pytania
# - answers_csv to ścieżka pliku, który zawiera odpowiedzi
# Funkcja zwraca liczbę poprawnych odpowiedzi
import csv
def check_homework(capitals_csv, questions_csv, answers_csv):
    with open(capitals_csv, 'r') as stolice, open(questions_csv, 'r') as pytania, open(answers_csv, 'r') as odpowiedzi:
    	reader_answers = csv.reader(odpowiedzi, delimiter=';')
    	reader_questions = csv.reader(pytania, delimiter=';')
    	reader_capitals = csv.reader(stolice, delimiter=';')

    	next(reader_capitals)
    	next(reader_questions)
    	next(reader_answers)
    	questions = []
    	answers = []
    	capitals =[]
    	for row in reader_answers:
    		#print(row)
    		answers.append(*row)
    	for row2 in reader_questions:
    		questions.append(row2)
    	for row3 in reader_capitals:
    		capitals.append(row3)

    	# print(answers)
    	# print(questions)
    	# print(capitals)

    	temp = 0
    	kraje_stolice ={}
    	for i in capitals:
    		kraje_stolice[capitals[temp][0]] = capitals[temp][1]
    		temp = temp + 1

    	i = 0
    	poprawne_odp = 0
    	for odp in answers:

    		if odp =='A':
    			j = 1
    		elif odp =='B':
    			j = 2
    		elif odp =='C':
    			j = 3
    		elif odp =='D':
    			j = 4

    		kraj = questions[i][0]
    		stolica = questions[i][j]
    		i = i + 1

    		if kraje_stolice[kraj] == stolica:
    			poprawne_odp = poprawne_odp + 1
    return poprawne_odp


check_homework('stolice.csv', 'pytania.csv', 'odpowiedzi.csv')
assert check_homework('stolice.csv', 'pytania.csv', 'odpowiedzi.csv') == 7