# 1
for i in range(11):
    print(i, end=" ")


# 2
for i in range(10, -1, -1):
    print(i, end=" ")


# 3
for i in range(-10, -1, 2):
    print(i, end=" ")


# 4
for i in range(1, 20, 3):
    print(i, end=" ")


# 5
nums = map(int, input().split())
summ = 0

for num in nums:
    if num % 2 == 1:
        summ += num

print(summ)


# 6
cities = input().split()

for city in cities:
    print(len(city), end=" ")


# 7
n = int(input())

for possible_divisor in range(1, n + 1):
    if n % possible_divisor == 0:
        print(possible_divisor)


# 8
n = int(input())

for possible_divisor in range(2, n):
    if n % possible_divisor == 0:
        print("НЕТ")
        break
else:
    print("ДА")


# 9
cities = input().lower().split()
last_char = cities[0][0]

for city in cities:
    if last_char != city[0]:
        print("НЕТ")
        break
    last_char = city[-2] if city[-1] in ("ь", "ъ", "ы") else city[-1]
else:
    print("ДА")


# 10
print(
    sum(
        added
        for added in range(int(input()) - 1, 0, -1)
        if added % 3 == 0 or added % 5 == 0
    )
)
