T = int(input())

for i in range(T):
    arr = list(map(int, input().split()))
    arr.remove(max(arr))
    arr.remove(min(arr))
    print(f"#{i+1} {round(sum(arr)/len(arr))}")