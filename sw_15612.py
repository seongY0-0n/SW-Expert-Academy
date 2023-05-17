T = int(input())

for tc in range(1, T+1):
    rook = list()
    for a in range(8):
        rook.append(input())
    check = [False] * 8
    result = 'yes'
    for i in rook:
        if i.count('O') > 1:
            result = 'no'
            break
        if 'O' in i:
            if not check[i.index('O')]:
                check[i.index('O')] = True
            else:
                result = 'no'
                break
        else:
            result = 'no'
            break

    print(f"#{tc} {result}")