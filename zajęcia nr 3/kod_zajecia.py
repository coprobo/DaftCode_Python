# Klasy - OOP

# Klasy to rzeczowniki a funkcje to czasowniki (takie zalozenie przy nazewnictwie)

# Klasa jest pisana camel casem - czyli kazdy wyraz w nazwie klasy jest z duzej litery
#Np: ToJestMojaKlasa()

# Klasy są obiektami
# atrybuty - mozna do nich sie dostac przez kropke

#Dan klasa moze miec tykj==lko jednego innita

# class Person():
# 	def __init__(self, name, surname):
# 		self.name = name
# 		self.surname = surname

# janek = Person('Jan', 'Jankowski')
# piotr = Person('Piotr', 'Piotrowski')

# print(type(Person))

# for i in(janek, piotr):
# 	print(type(i), i.name, i.surname)


# class Surprise():
# 	a = 44
# 	b = []
# 	def __init__(self, name):
# 		self.name = name

# sup1 = Surprise('pierwsza')
# sup2 = Surprise('druga')

# def print_surprises():
# 	print(Surprise, Surprise.a, Surprise.b) # ,Suprise.name) <- tego sie nie da bo jeszcze nie jest dostepne
# 	print(sup1, sup1.a, sup1.b, sup1.name)
# 	print(sup2, sup2.a, sup2.b, sup2.name)

# sup1.a = 23
# print_surprises()

#########################################################


class Vector():
	def __init__(self, *args):
		self.coords = list(args)

	def __len__(self):
		return len(self.coords)

	def __repr__(self):
		template = '{}({})'
		name = self.__class__.__name__
		args = ','.join(repr(x) for x in self.coords)
		#print(name, args)
		return template.format(name, args)

	def __add__(self, other):
		tmp = []
		for i in range(len(self)):
			tmp.append(self.coords[i] + other.coords[i])
		return Vector(*tmp)

	def __iadd__(self, other):
		for i in range(len(self)):
			self.coords[i] += other.coords[i]
		return self

	def __eq__(self, other):
		equal = True
		for i in range(len(self)):
			if not self.coords[i] == other.coords[i]:
				return False
		return True



v = Vector(1, 2, 3)

v1 = Vector(1, 2, 3)

print('len(Vector(1,2, 3)) : ', len(Vector(1,2, 3)))
print('len(Vector(1)): ', len(Vector(1)))

print('v: ', v)
print('v1:', v1)

v3 = v1 + v
print(id(v1))
print(id(v))
print(id(v3))
print('v3=', v3)

v3 += v
print(id(v3))

print('v1 == v: ', v1==v)