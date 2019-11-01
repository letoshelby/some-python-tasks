# Дан список стран и городов каждой страны. Затем даны названия городов. Для каждого города укажите, в какой стране он находится.


countries = {}

for i in range(int(input())):
	key, *values = input().split()
	countries[key] = values

for i in range(int(input())):
	city_name = input()
	[print(i) for i in countries if city_name in countries[i]]
