T = int(input())

for i in range(1, T+1):
    h1, m1, h2, m2 = map(int, input().split())
    h3, m3 = 0, 0

    if m1 + m2 < 60:
        m3 = m1 + m2
    else:
        m3 = m1 + m2 - 60
        h3 += 1

    if h1 + h2 + h3 < 13:
        h3 += h1 + h2
    else:
        h3 += h1 + h2 - 12
    print(f"#{i} {h3} {m3}")