T = int(input())

for tc in range(1, T+1):
    N = int(input())
    ms = 0
    result = 0
    for i in range(N):
        arr = list(map(int, input().split()))
        if arr[0] == 1:
            ms += arr[1]
            result += ms
        elif arr[0] == 2:
            if ms - arr[1] > 0:
                ms -= arr[1]
            else:
                ms = 0

            result += ms
        else:
            result += ms

    print(f"#{tc} {result}")