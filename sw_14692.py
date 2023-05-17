T = int(input())

for tc in range(1, T+1):
    S = input()
    result = 0
    arr = list(S)

    for i in range(len(arr)-1):
        if arr[i] == '(':
            if arr[i+1] =='|' or arr[i+1] == ')':
                result+=1
        elif arr[i] == '|' and arr[i+1] == ')':
            result+=1

    print(f"#{tc} {result}")