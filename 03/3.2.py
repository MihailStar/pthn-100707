# 1
string = input()

print(f"{string[0]}{string[-1]}")


# 4
string = input()

print(string[:4])


# 5
string = input()

print(string[-3:])


# 6
string = input()

print(string[1::2])


# 7
string1, string2 = input(), input()

print(string1[::2] + " " + string2[1::2])


# 8
string = input()

print(string[4::-1])


# 9
word1, word2 = input().split()

print(word2[: len(word1)])


# 10
word1, word2 = input().split()

print(word1[1 : len(word2) : 2] == word2[1::2])
