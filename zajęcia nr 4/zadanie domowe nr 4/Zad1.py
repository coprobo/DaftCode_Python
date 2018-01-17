# Zaimplementuj klasę Date, która tworzona jest na podstawie trzech wartości - day, month i year.
# Obiekt klasy powinien zawierać atrybuty day, month i year

# Twoim zadaniem jest sprawdzenie w trakcie tworzenia obiektu, czy podane wartości są poprawne:
# jeśli year nie jest intem - rzucić InvalidYearError
# jeśli month nie jest intem lub nie zawiera się w przedziale od 1 do 12 - rzucić InvalidMonthError
# jeśli day nie jest intem lub nie zawiera się w przedziale o 1 do 28/30/31 (odpowiednio w zależności od miesiąca) - rzucić InvalidDayError

# Wszystkie opisane powyżej błędy powinny dziedziczyć z bazowego błędu - DateError

# W zadaniu dla uproszczenia zakładamy, że każdy luty ma 28 dni ;)

class DateError(Exception):
	pass

class InvalidYearError(DateError):
    pass

class InvalidMonthError(DateError):
	pass

class InvalidDayError(DateError):
	pass

class Date():
	def __init__(self, day, month, year):
		if type(year) != int:
			raise InvalidYearError
		elif year < 0:
			raise InvalidYearError
		else:
			self.year = year

		if type(month) != int:
			raise InvalidMonthError
		elif month>0 and month<13:
			self.month = month
		else:
			raise InvalidMonthError			

		if type(day) != int:
			raise InvalidDayError
		#sprawdzam czy miesiac nalezy od 1 do 12
		elif month in [1,2,3,4,5,6,7,8,9,10,11,12]:
			#sprawdzam miesiace 31 dniowe
			if month in [1, 3, 5, 7, 8, 10, 12]:
				if day>0 and day<32:
					self.day = day
				else:
					raise InvalidDayError
			#sprawdzam miesiace 30 dniowe
			elif month in [4, 6, 9, 11]:
				if day>0 and day<31:
					self.day = day					
				else:
					raise InvalidDayError
			if month == 2:
				if day>0 and day<29:
					self.day = day
				else:
					raise InvalidDayError		


