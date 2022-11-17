
T = int(input())

for i in range(T):
    N, K = map(int, input().split())
    arr = [0] * N
    score = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    for j in range(N):
        a, b, c = map(int, input().split())
        arr[j] = a * 35 + b * 45 + c * 20

    temp = arr[K-1]
    arr.sort(reverse=True)

    print(f"#{i+1} {score[arr.index(temp)//int(N/10)]}")