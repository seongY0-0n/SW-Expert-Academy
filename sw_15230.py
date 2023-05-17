T = int(input())

for tc in range(1, T+1):
    Al = 'abcdefghijklmnopqrstuvwxyz'
    result = 0
    word = input()
    idx = 0
    for i in Al:
        if idx < len(word) and word[idx] == i:
            result += 1
            idx += 1
        else:
            break
    print(f"#{tc} {result}")