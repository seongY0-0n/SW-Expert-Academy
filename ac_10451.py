tc = int(input())


def dfs(v):
    visited[v] = True
    if not visited[graph[v]]:
        dfs(graph[v])



for _ in range(tc):
    N = int(input())
    P = list(map(int, input().split()))
    visited = [False] * (N + 1)
    answer = 0
    graph = [0] * (N + 1)
    for i in range(N):
        graph[P[i]] = P[P[i] - 1]

    for i in range(1, N + 1):
        if not visited[i]:
            dfs(i)
            answer += 1

    print(answer)
