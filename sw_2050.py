alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
arr = list(alpha)

word = input()
num = list()
for s in word:
    num.append(arr.index(s)+1)

print(*num)