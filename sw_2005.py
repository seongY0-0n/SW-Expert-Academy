T = int(input())

for i in range(T):
    arr = list()
    s = int(input())
    arr.append([1])
    arr.append([1, 1])
    for j in range(2, s):
        temp = list()
        temp.append(1)
        for k in range(1, j):
            temp.append(arr[j-1][k-1] + arr[j-1][k])

        temp.append(1)
        arr.append(temp)
    print("#" + str(i+1))
    for j in range (s):
        print(*arr[j])
