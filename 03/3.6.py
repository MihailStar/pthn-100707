# 3
print([*map(int, input().split())])


# 4
cities = input().split()

print("Москва" in cities)


# 6
cities = input().split()

print(cities[-1])


# 7
marks = list(map(int, input().split()))

print(round(sum(marks) / len(marks), 1))


# 8
book = [input(), input(), int(input()), float(input())]
del book[2]
book[1] = "Пушкин"
book[-1] = book[-1] * 2

print(book)


# 9
subscribers = list(map(int, input().split()))

print(max(subscribers), min(subscribers), sum(subscribers))


# 10
subscribers = sorted(map(int, input().split()), reverse=True)

print(*subscribers)


# 12
cities = ["Москва", "Тверь", "Вологда"]
cities += input().split()

print(*cities)


# 13
cities = ["Москва", "Тверь", "Вологда"]

print(*input().split() + cities)
