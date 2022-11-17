T = int(input())

for i in range(T):
    s = input()
    arr = list(s)
    result = True
    for j in range(len(arr)//2):
        if arr[j] != arr[-1-j]:
            result = False
            break

    if result:
        print(f"#{i+1} 1")
    else:
        print(f"#{i+1} 0")