# 2
digits = input().split()

digits.append(digits[0] != digits[-1])

print(*digits)


# 3
cities = ["Москва", "Казань", "Ярославль"]
cities.insert(1, "Ульяновск")

print(*cities)


# 4
lst = list(input())
del lst[0]
lst[0] = "8"
lst = [char for char in lst if char != "-"]

print("".join(lst))


# 5
i, o, f = input().split()


print(f"{f} {i[0]}.{o[0]}.")


# 7
print(*sorted(map(int, input().split()))[:3])


# 8
nums = input().split()
nums[-1] = int(nums[-1]) % 2 != 0

print(*nums)


# 9
print(input().split().count("2"))


# 10
print(*sorted(input().split())[1:])
