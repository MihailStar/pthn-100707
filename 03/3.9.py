# 1
a = [5.4, 6.7, 10.4]

a.append(list(map(int, input().split())))

print(a)


# 2
print([input().split(), input().split(), input().split()])


# 3
matrix = [
    input().split(),
    input().split(),
    input().split(),
]

print(*[int(row[len(row) - 1]) for row in matrix])


# 6
word = input()

t = [
    ["Скажи-ка", "дядя", "ведь", "не", "даром"],
    ["Я", "Python", "выучил", "с", "каналом"],
    ["Балакирев", "что", "раздавал?"],
]

print(any([word in row for row in t]))
