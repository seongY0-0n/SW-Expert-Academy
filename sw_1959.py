T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    result = list()

    if len(A) < len(B):
        for i in range(len(B)-len(A)+1):
            temp = 0
            for j in range(len(A)):
                temp += A[j]*B[j+i]
            result.append(temp)
    else:
        for i in range(len(A)-len(B)+1):
            temp = 0
            for j in range(len(B)):
                temp += B[j]*A[j+i]
            result.append(temp)
    print(f"#{tc} {max(result)}")