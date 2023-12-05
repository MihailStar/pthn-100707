# 3
width = int(input())


def func1() -> int:
    global width
    width += 1

    return width


print(func1())


# 4
def func1() -> None:
    msg = input()

    def func2() -> None:
        nonlocal msg
        msg = input()
        print(msg)

    func2()

    print(msg)


func1()


# 5
def create_global(x: str) -> None:
    global TOTAL
    TOTAL = x
