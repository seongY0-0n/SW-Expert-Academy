T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list()
    result = 'possible'
    for _ in range(N):
        arr.append(list(input()))

    for a in arr:
        if '##' in "".join(a) or '..' in "".join(a):
            result = 'impossible'
            break

    print(f"#{tc} {result}")