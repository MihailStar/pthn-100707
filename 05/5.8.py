# 1
lst = [abs(float(n)) for n in input().split()]

print(lst)


# 2
lst = [int(d) for d in input()]

print(lst)


# 3
n = int(input())

for row in [[1 if x == y else 0 for x in range(n)] for y in range(n)]:
    print(*row)


# 4
cities = input().split()

print(*[city for city in cities if len(city) > 5])


# 5
n = int(input())

print(*[d for d in range(1, n + 1) if n % d == 0])


# 6
n = int(input())

for row in [[y for _x in range(n)] for y in range(n)]:
    print(*row)


# 7
print(*[d for i, d in enumerate(input().split()) if i % 2 == 0])


# 8
print(*[int(a) + int(b) for a, b in zip(input().split(), input().split())])


# 9
inputed_data = input().split()

print(
    [
        [inputed_data[i], int(inputed_data[i + 1])]
        for i in range(0, len(inputed_data) - 1, 2)
    ]
)
