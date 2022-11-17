T = int(input())

for i in range(T):
    n = int(input())
    temp = 0
    for i in range(1,n+1):
        if i % 2 == 0:
            temp -= i
        else:
            temp +=i

    print(f"#{i+1} {temp}")