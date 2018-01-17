# Requests: Wszystkie postaci z “Gwiezdnych Wojen”
#
# Na podstawie API: https://swapi.co/ napisz generator listujący wszystkie postaci pochodzące
# z sagi Star Wars `sw_person_generator`. Postaci zwracaj wg kolejności z API.
# Jeśli generator nie będzie mógł się połączyć z API, to powinien się zakończyć - generacja osób nie jest możliwa.
# Proszę użyć modułu requests.

import requests
from pprint import pprint
from requests.exceptions import RequestException

url = 'https://swapi.co/api/people/{person_id}/'


def get_sw_chars():
	people_found = 1
	people_not_found_in_row = 0

	while True:
		current_url = url.format(person_id = people_found)

		try:
			r = requests.get(url = current_url)

		except RequestException:
			return

		people_found +=1

		print(r.status_code, current_url)

		if r.ok:
			people_not_found_in_row = 0
			person = r.json()
			yield person.get('name')
			print(person.get('name'))

		elif r.status_code == 404:
			people_not_found_in_row += 1

			if people_not_found_in_row > 5:
				return
			else:
				continue
		else:
			return




if __name__ == '__main__':
    assert list(get_sw_chars()) == ['Luke Skywalker', 'C-3PO', 'R2-D2', 'Darth Vader', 'Leia Organa', 
    'Owen Lars', 'Beru Whitesun lars', 'R5-D4', 'Biggs Darklighter', 'Obi-Wan Kenobi', 'Anakin Skywalker', 
    'Wilhuff Tarkin', 'Chewbacca', 'Han Solo', 'Greedo', 'Jabba Desilijic Tiure', 'Wedge Antilles', 
    'Jek Tono Porkins', 'Yoda', 'Palpatine', 'Boba Fett', 'IG-88', 'Bossk', 'Lando Calrissian', 'Lobot', 'Ackbar', 
    'Mon Mothma', 'Arvel Crynyd', 'Wicket Systri Warrick', 'Nien Nunb', 'Qui-Gon Jinn', 'Nute Gunray', 'Finis Valorum', 
    'Padmé Amidala', 'Jar Jar Binks', 'Roos Tarpals', 'Rugor Nass', 'Ric Olié', 'Watto', 'Sebulba', 'Quarsh Panaka', 'Shmi Skywalker', 
    'Darth Maul', 'Bib Fortuna', 'Ayla Secura', 'Ratts Tyerell', 'Dud Bolt', 'Gasgano', 'Ben Quadinaros', 'Mace Windu', 'Ki-Adi-Mundi', 
    'Kit Fisto', 'Eeth Koth', 'Adi Gallia', 'Saesee Tiin', 'Yarael Poof', 'Plo Koon', 'Mas Amedda', 'Gregar Typho', 'Cordé', 'Cliegg Lars', 
    'Poggle the Lesser', 'Luminara Unduli', 'Barriss Offee', 'Dormé', 'Dooku', 'Bail Prestor Organa', 'Jango Fett', 'Zam Wesell', 'Dexter Jettster', 
    'Lama Su', 'Taun We', 'Jocasta Nu', 'R4-P17', 'Wat Tambor', 'San Hill', 'Shaak Ti', 'Grievous', 'Tarfful', 'Raymus Antilles', 'Sly Moore', 'Tion Medon', 
    'Finn', 'Rey', 'Poe Dameron', 'BB8', 'Captain Phasma']
