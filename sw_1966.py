T = int(input())

for t in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    print(f"#{t} {' '.join(str(a) for a in arr)}")