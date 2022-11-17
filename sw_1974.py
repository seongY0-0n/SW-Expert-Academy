def check_sdoku(arr):
    if 1 in arr and 2 in arr and 3 in arr and 4 in arr and 5 in arr and 6 in arr and 7 in arr and 8 in arr and 9 in arr:
        return True
    else:
        return False

T = int(input())

for t in range(1, T+1):
    sdoku = list()
    result = True
    for _ in range(9):
        sdoku.append(list(map(int, input().split())))

    for i in sdoku:
        if not check_sdoku(i):
            result = False

    for i in range(9):
        temp = list()
        for j in range(9):
            temp.append(sdoku[j][i])
        if not check_sdoku(temp):
            result = False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            temp = list()
            for k in range(3):
                for l in range(3):
                    temp.append(sdoku[i+k][j+l])

            if not check_sdoku(temp):
                result = False

    if result:
        print(f"#{t} 1")
    else:
        print(f"#{t} 0")









