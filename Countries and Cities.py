countries = {}

for i in range(int(input())):
	key, *values = input().split()
	countries[key] = values

for i in range(int(input())):
	city_name = input()
	[print(i) for i in countries if city_name in countries[i]]
