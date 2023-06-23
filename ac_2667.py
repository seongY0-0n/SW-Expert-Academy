from collections import deque

def bfs(x,y,arr):
    arr[x][y]=0
    q = deque()
    q.append((x,y))
    count = 1
    while q:
        x, y = q.popleft()
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            if arr[nx][ny] == 0:
                continue

            q.append((nx,ny))
            arr[nx][ny] = 0
            count += 1

    return count


N = int(input())

arr = list()

for i in range(N):
    arr.append(list(map(int, input())))

answer = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            answer.append(bfs(i,j,arr))

print(len(answer))
answer.sort()
for i in answer:
    print(i)



