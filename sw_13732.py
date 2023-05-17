T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list()
    v = True
    result = 'yes'
    a, b = 0, 0
    for _ in range(N):
        arr.append(list(input()))
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '#':
                a, b = i, j
                v = False
                break
        if not v:
            break
    v = True
    count = 0
    for j in range(b, N):
        if arr[a][j] == '#':
            count += 1
        else:
            break

    for i in range(a, a+count):
        for j in range(b, b+count):
            if arr[i][j] != '#':
                result = 'no'
            else:
                arr[i][j] = '.'

    for i in arr:
        if '#' in i:
            result = 'no'

    print(f"#{tc} {result}")




