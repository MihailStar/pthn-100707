# 1
gen = (n for n in range(2, 10_000 + 1))


# 2
a, b = map(int, input().split())
tp = tuple((n**2 for n in range(a, b + 1)))


# 3
a, b = map(int, input().split())
gen = (abs(n) for n in range(a, b + 1))

for _ in range(5):
    print(next(gen))


# 6
a = int(input())
gen = (n**3 for n in (abs(n) for n in range(-a, a + 1)))

for _ in range(4):
    print(next(gen), end=" ")


# 7
from string import ascii_lowercase

gen = (f"{a}{b}" for a in ascii_lowercase for b in ascii_lowercase)

for _ in range(50):
    print(next(gen), end=" ")


# 8
cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]
gen = (cities[i % len(cities)] for i in range(1_000_000 + 1))

for _ in range(20):
    print(next(gen), end=" ")


# 9
a, b = map(int, input().split())
gen = (
    round(0.5 * pow(x / 100, 2) - 2.0, 2)
    for x in range(a * 100, b * 100 + 1, int(0.01 * 100))
)

print(*(next(gen) for _ in range(20)), end="")
