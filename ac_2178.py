from collections import deque


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()

        if miro[x][y] == 0:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            if miro[nx][ny] == 0 or visited[nx][ny]:
                continue
            queue.append((nx, ny))
            visited[nx][ny] = True
            miro[nx][ny] = miro[x][y] + 1


N, M = map(int, input().split())
answer = 0
miro = []
visited = list()
for i in range(N):
    visited.append([False] * M)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(N):
    miro.append(list(map(int, input())))

bfs(0, 0)
print(miro[-1][-1])
