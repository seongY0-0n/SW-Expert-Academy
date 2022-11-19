T = int(input())

for tc in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())
    A_price = P * W

    if W < R:
        B_price = Q
    else:
        B_price = Q + S * (W - R)

    print(f"#{tc} {min(A_price, B_price)}")
