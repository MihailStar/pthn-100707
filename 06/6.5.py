# 1
a = set(int(n) for n in input().split())
b = set(int(n) for n in input().split())

print(*sorted(a & b))


# 2
a = set(int(n) for n in input().split())
b = set(int(n) for n in input().split())

print(*sorted(a - b))


# 3
a = set(int(n) for n in input().split())
b = set(int(n) for n in input().split())

print(*sorted(a ^ b))


# 4
a = set(input().split())
b = set(input().split())

print("ДА" if a == b else "НЕТ")


# 5
grades = [int(n) for n in input().split()]

print(f"{'НЕ ' if set(grades) & {2} else ''}ДОПУЩЕН")


# 6
a = set(input().split())
b = set(input().split())

print("ДА" if a.issubset(b) else "НЕТ")


# 7
n = int(input())

print("ДА" if n % 2 == 0 and n % 3 == 0 and n % 5 == 0 else "НЕТ")
