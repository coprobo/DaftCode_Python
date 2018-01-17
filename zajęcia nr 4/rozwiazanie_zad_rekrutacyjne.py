import csv


with open('conferences_data.csv', 'r') as csv_file:
	d = {}
	reader = csv.reader(csv_file, delimiter = ';')
	next(reader) #przeskakujemy header, nazwy konferencji
	for row in reader:
		print(row)
		for conf, email in enumerate(row): #dostejemy indeks i wartosc
			if not email:
				continue
			try:
				conferences = d[email]
			except KeyError:
				conferences = set()
				d[email] = conferences
			conferences.add(conf)
# print(d)

def get_country_from_email(email):
	_, rest = email.split('@') #podkreslnik oznacza ze to nas nie interesuje, przypisujemy cos do _ ale pozniej nie uzyjemy
	_, country = rest.split('.')
	return country

def get_company_from_email(email):
	_, rest = email.split('@') #podkreslnik oznacza ze to nas nie interesuje, przypisujemy cos do _ ale pozniej nie uzyjemy
	company, _ = rest.split('.')
	return company

result1 = len([email for email in d if len(d[email]) > 1])
print(result1)

result2 = len([email for email in d if get_company_from_email(email) == 'wok'])
print(result2)

result3 = len(set([get_country_from_email(email) for email in d]))
print(result3)
#albo
result3_2 = len({get_country_from_email(email) for email in d})
print(result3_2)

