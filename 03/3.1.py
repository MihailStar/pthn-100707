# 5
string1 = input()
string2 = input()

print(string1, string2)


# 7
word1, word2 = input().split()

print((word1 + " ") * 2, (word2 + " ") * 3, sep="")


# 8
num1, num2 = map(int, input().split())

print("Переменная a = " + str(num1) + ", переменная b = " + str(num2))


# 9
words = input()

print("Строка: " + words + ". Длина: " + str(len(words)))


# 10
word1, word2 = input().split()

print(word1 in word2, word1 == word2, word1 > word2, word1 < word2)


# 11
char1, char2 = input().split()

print(f"Коды: {char1} = {ord(char1)}, {char2} = {ord(char2)}")
