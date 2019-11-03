def count_capitals(string):
	count = 0
	for symbol in string:
		if symbol.isupper():
			count += 1
	return count


count_of_error = 0
list_words = []

for word in range(int(input())):
	list_words.append(input())

for word in input().split():
	if word in list_words:
		print(word)
	else:
		if count_capitals(word) == 1:
			pass
		else:
			count_of_error += 1

print(count_of_error)





