T = int(input())

for i in range(T):
    n, m = map(int, input().split())
    arr = list()
    for j in range(n):
        arr.append(list(map(int, input().split())))
    maxi = 0
    for x in range(n-m+1):
        for y in range(n-m+1):
            temp = 0

            for z in range(m):
                for e in range(m):
                    temp += arr[x+z][y+e]

            if temp > maxi:
                maxi = temp
    print("#{0} {1}".format(i+1, maxi))