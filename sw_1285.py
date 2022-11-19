T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i] *= (-1)

    print(f"#{tc} {min(arr)} {arr.count(min(arr))}")