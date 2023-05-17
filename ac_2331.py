def dfs(v):
    nxt = 0
    while v > 0:
        temp = v % 10
        nxt += temp ** P
        v = v // 10

    if nxt in graph:
        graph.append(nxt)
        return
    else:
        graph.append(nxt)
        dfs(nxt)


A, P = map(int, input().split())

graph = [A]
dfs(A)

temp = graph.pop()

print(graph.index(temp))