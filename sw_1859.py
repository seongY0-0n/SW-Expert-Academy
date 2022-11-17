T = int(input())
for i in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    maxi = arr[-1]
    result = 0
    for j in range(N-2,-1,-1):
        if arr[j] > maxi:
            maxi = arr[j]
        else:
            result += maxi - arr[j]

    print("#{0} {1}".format(i+1, result))