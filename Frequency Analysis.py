import random

def random_nick():
	""" Сгенерировать ник (имя юзера). [Модификация: http://codepaste.ru/3853/]"""

	vowels = 'aeuioy'
	covowels = 'qwrtpsdfghjklzxcvbnm'

	syllables = [[], []]

	# Состовляем таблицу возможных

	for vowel in vowels:
		for covowel in covowels:

			if vowel != 'y':
				syllables[0].append(vowel + covowel)

			syllables[1].append(covowel + vowel)

	nick = ""  # Сам ник
	d = True

	for i in range(0, random.randint(3, 4)):
		# Строим слово по слогам

		d = not d
		nick += random.choice(syllables[int(d)])
		d = random.randint(0, 9) > 7 or nick[-1] == 'y'

	if random.randint(0, 9) > 4:
		# Добавляем последнию букву

		c = d and covowels or vowels
		nick += random.choice(c)

	return nick


print(random_nick())