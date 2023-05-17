def dfs (x,y):

    if x < 0 or y < 0 or x >= N or y >= M:
        return False

    if ice[x][y] == 0:
        ice[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        dfs(x+1,y)
        return True
    return False


N, M = map(int, input().split())
ice = []

for i in range(N):
    ice.append(list(map(int, input().split())))

answer = 0
for i in range(N):
    for j in range(M):
        if dfs(i,j):
            answer +=1
print(answer)