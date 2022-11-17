T = int(input())

for i in range(T):
    n = int(input())
    temp = 0
    for j in range(1,n+1):
        if j % 2 == 0:
            temp -= j
        else:
            temp += j

    print(f"#{i+1} {temp}")