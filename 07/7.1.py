# 3
def func3() -> None:
    print("It's my first function")


func3()


# 4
имя, фамилия = input().split()


def func4() -> None:
    print(f"Уважаемый, {имя} {фамилия}! Вы верно выполнили это задание!")


func4()


# 5
weight = float(input())


def func5(weight: float) -> None:
    print(f"Предмет имеет вес: {weight} кг.")


func5(weight)


# 6
from typing import List

nums = [int(digs) for digs in input().split()]


def func6(nums: List[int]) -> None:
    print(f"Min = {min(nums)}, max = {max(nums)}, sum = {sum(nums)}")


func6(nums)


# 7
def func7(width: int, height: int) -> None:
    print(f"Периметр прямоугольника, равен {width * 2 + height * 2}")


func7(*(int(dig) for dig in input().split()))


# 8
import re as regexp

pattern = regexp.compile(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.[a-zA-Z0-9_]+$")


def func8(email: str) -> None:
    print("НЕТ" if pattern.match(email) == None else "ДА")


func8(input())
