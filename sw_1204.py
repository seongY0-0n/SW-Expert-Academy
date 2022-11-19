T = int(input())

for tc in range(1, T+1):
    n = int(input())
    result = list()
    score = list(map(int, input().split()))
    score_num = [0]*101

    for i in set(score):
        score_num[i] = score.count(i)

    maxi = max(score_num)
    while max(score_num) == maxi:
        result.append(score_num.index(max(score_num)))
        score_num[score_num.index(max(score_num))] = 0

    print(f"#{tc} {max(result)}")