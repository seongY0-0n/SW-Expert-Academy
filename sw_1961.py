T = int(input())

for t in range(1, T+1):
    n = int(input())
    result1 = [[0 for _ in range(n)] for _ in range(n)]
    result2 = [[0 for _ in range(n)] for _ in range(n)]
    result3 = [[0 for _ in range(n)] for _ in range(n)]

    arr = list()
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    for i in range(n):
        for j in range(n):
            result1[i][j] = arr[n-1-j][i]
    for i in range(n):
        for j in range(n):
            result2[i][j] = result1[n-1-j][i]
    for i in range(n):
        for j in range(n):
            result3[i][j] = result2[n-1-j][i]

    print(f"#{t}")
    for i in range(n):
        for a in range(n):
            print(result1[i][a], end='')
        print(end=' ')
        for b in range(n):
            print(result2[i][b], end='')
        print(end=' ')
        for c in range(n):
            print(result3[i][c], end='')
        print()


