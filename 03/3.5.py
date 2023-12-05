# 1
print(
    "Уважаемый {} {}! Поздравляем Вас с {}-летием!".format(
        input(), input(), int(input())
    )
)


# 2
width, depth, height = map(int, input().split())

print(
    "Габариты: {width} x {depth} x {height}".format(
        **{
            "width": width,
            "depth": depth,
            "height": height,
        }
    )
)


# 3
numbers = input()

print(" ".join(sorted(numbers.split())))


# 4
city, street, house, flat = input(), input(), input(), input()

print(f"г. {city}, ул. {street}, д. {house}, кв. {flat}")


# 5
from math import floor

r_to_d, r = float(input()), int(input())
d = r / r_to_d

print(f"Вы можете получить {floor(d)}$ за {r} рублей по курсу {r_to_d}")
