T = int(input())

for t in range(1, T+1):
    n, k = map(int, input().split())
    result = 0
    ans = '1'*k
    arr = list()
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    for i in range(n):
        count = 0
        for j in range(n):
            if arr[i][j] == 1:
                count += 1
            if arr[i][j] == 0 or j == n-1:
                if count == k:
                    result += 1
                count = 0
        for j in range(n):
            if arr[j][i] == 1:
                count += 1
            if arr[j][i] == 0 or j == n-1:
                if count == k:
                    result += 1
                count = 0
    print(f"#{t} {result}")