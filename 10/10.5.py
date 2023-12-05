# 4
t = (int, str, str, float, int)
book = [t[i](x) if t[i] != str else x.strip() for i, x in enumerate(input().split(","))]

match book:
    case [int(), str(), str()] | [int(), str(), str(), float()]:
        print("Yes")
    case [int(), str(), str(), int()] | [int(), str(), str(), float(), int()]:
        print("Yes")
    case _:
        print("No")


# 5
t = (int, str, str, float, int)
book = [t[i](x) if t[i] != str else x.strip() for i, x in enumerate(input().split(","))]

match book:
    case int(), str() as author, str() as title if len(author) > 5 and len(title) > 9:
        print("Yes")
    case int(), str() as author, str(), float() as price if len(
        author
    ) > 5 and price > 0:
        print("Yes")
    case int(), str(), str(), int() as year if year > 2019:
        print("Yes")
    case int(), str(), str(), float() as price, int() as year if price > 0 and year > 2019:
        print("Yes")
    case _:
        print("No")
