N = int(input())
arr = list()
for i in range(1,N+1):
    w = ""
    for s in str(i):
        if s == "3" or s == "6" or s == "9":
            w += "-"

    if w == "":
        arr.append(str(i))
    else:
        arr.append(w)
print(*arr)
