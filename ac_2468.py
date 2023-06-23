from collections import deque
import copy

def bfs(x,y,temp):
    temp[x][y] = 0
    q = deque()
    q.append((x,y))

    while q:
        x, y = q.popleft()
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if temp[nx][ny] == 0:
                continue
            q.append((nx,ny))
            temp[nx][ny] = 0



n = int(input())

arr= []

for i in range(n):
    arr.append(list(map(int,input().split())))



result = []
for i in range(min(map(min, arr)), max(map(max, arr))):
    temp = []
    temp = copy.deepcopy(arr)
    answer = 0

    for j in range(n):
        for k in range(n):
            if temp[j][k] <= i:
                temp[j][k] = 0

    for j in range(n):
        for k in range(n):
            if temp[j][k] != 0:
                bfs(j, k, temp)
                answer +=1
    result.append(answer)

print(max(result))