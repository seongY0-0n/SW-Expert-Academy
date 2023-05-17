T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input().split())) for _ in range(N)]

    word = ""

    for i in range(N):
        for j in range(int(arr[i][1])):
            word += arr[i][0]
    count = 0
    temp = ""
    print(f"#{tc}")
    for w in word:
        temp += w
        count += 1

        if count == 10:
            print(temp, end='\n')
            count = 0
            temp = ""
    if temp != "":
        print(temp)