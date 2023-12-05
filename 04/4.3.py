# 1
n1 = float(input())
n2 = float(input())

print(n1 if n1 > n2 else n2)


# 2
n = float(input())

print("кратно 3" if n % 3 == 0 else "не кратно 3")


# 3
word = input().lower()

print("палиндром" if word == word[::-1] else "не палиндром")


# 4
print("True" if input() == "1" else "False")


# 5
s = int(input())

print((s + 1) % 60)


# 6
m = ["до", "ре", "ми", "фа", "соль", "ля", "си"]

print(
    *[
        "#" + m[i] if m[i] in ["до", "фа"] else m[i]
        for i in map(lambda digit: int(digit) - 1, input().split())
    ]
)
