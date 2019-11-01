counter = {}

for i in range(int(input())):
    string = input().split()
    for word in string:
        counter[word] = counter.get(word, 0) + 1


sorted_list = (sorted(counter.items(), key=lambda item: (-item[1], item[0])))

for word, amount in sorted_list:
    print(word)

