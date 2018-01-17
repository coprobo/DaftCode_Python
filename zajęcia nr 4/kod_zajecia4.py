# class IncorectGuessError(Exception):
# 	def __init__(self, difference):
# 		super().__init__()
# 		self.difference = difference

# class NumberTooSmallError(IncorectGuessError):
# 	pass

# class NumberTooBigError(IncorectGuessError):
# 	pass


# def guess(number):
# 	number_to_guess = 10
# 	if number > number_to_guess:
# 		raise NumberTooBigError(
# 			number - number_to_guess)
# 	elif number < number_to_guess:
# 		raise NumberTooSmallError(
# 			number - number_to_guess)
	
# 	print('Bravo!')


# try:
# 	guess(8)
# except NumberTooSmallError as nts:
# 	print('za malo o: {}'.format(nts.difference))
# except NumberTooBigError as ntb:
# 	print('Za duzo o: {}'.format(ntb.difference))

# with open('multiline_file.txt', 'a') as file:
# 	# print(file.readline(), end='')
# 	# print(file.readline(), end='')
# 	# print(file.readline(), end='')

# 	# for line in file: #iteruje po liniach w pliku
# 	# 	print(line, end='')
# 	file.write('\n APPEND Nowa linia \n')

#https://www.gutenberg.org/ebooks/31536 Pan Tadeusz w txt

from collections import Counter

with open('pan_tadeusz.txt', encoding = 'utf8') as file:
	counter = Counter()
	for line in file:
		words = line.split()
		counter.update(words)
print(counter.most_common(10))


