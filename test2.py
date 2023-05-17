from collections import deque
def dfs(V):

    visited[V] = True
    print(V, end=' ')

    for i in graph[V]:
        if not visited[i]:
            dfs(i)

def bfs(V):
    queue = deque()
    queue.append(V)
    visited[V] = True

    while queue:
        temp = queue.popleft()
        print(temp, end=' ')
        for i in graph[temp]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


N, M, V = map(int,input().split())
visited = [False] * (N+1)
graph = [[] for _ in range(N+1)]

for i in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in graph:
    i.sort()
dfs(V)
print()
visited = [False] * (N+1)
bfs(V)