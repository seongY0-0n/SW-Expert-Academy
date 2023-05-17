from itertools import permutations
T = int(input())

for tc in range(1, T+1):
    N = input()
    arr = list((permutations(N, len(N))))
    str_arr = list()
    temp = int(N) * 2
    result = False
    for i in range(len(arr)):
        str_arr.append("".join(arr[i]))

    while temp < int(max(str_arr)):
        if str(temp) in str_arr:
            result = True
            break
        temp = temp + int(N)
    if result:
        result = "possible"
    else:
        result = "impossible"

    print(f"#{tc} {result}")



