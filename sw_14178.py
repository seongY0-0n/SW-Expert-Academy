T = int(input())

for tc in range(1, T+1):
    N, D = map(int, input().split())
    result = 0
    if N % (D*2+1) == 0:
        result = N // (D*2+1)
    else:
        result = N // (D*2+1) + 1

    print(f"#{tc} {result}")