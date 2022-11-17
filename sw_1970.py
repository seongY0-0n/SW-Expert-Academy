T = int(input())

for t in range(1, T+1):
    N = int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    result = list()

    for i in money:
        result.append(N//i)
        N = N % i
    print("#", t, sep="")
    print(*result)