T = int(input())

for tc in range(1, T+1):
    N = int(input())
    check = [0] * 10
    idx = 0
    result = N
    while True:
        for s in str(result):
            if check[int(s)] == 0:
                check[int(s)] = 1
        if 0 not in check:
            break
        result += N

    print(f"#{tc} {result}")
