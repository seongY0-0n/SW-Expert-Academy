T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [0]*5
    temp = [2, 3, 5, 7, 11]
    index = 0
    for i in temp:
        while True:
            if N % i == 0:
                arr[index] += 1
                N = N // i
            else:
                index += 1
                break
    print("#", tc , sep="", end=" ")
    print(arr[0], arr[1], arr[2], arr[3], arr[4], sep=" ")
