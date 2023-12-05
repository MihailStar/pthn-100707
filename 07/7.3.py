# 1
def get_nod(a: int, b: int) -> int:
    """Находит наибольший общий делитель (НОД) двух натуральных чисел a и b"""

    while b != 0:
        a, b = b, a % b
    return a
