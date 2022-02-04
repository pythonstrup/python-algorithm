from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

visit = [False] * (n+1)

def dfs(graph, visited, v):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, visited, i)


def bfs(graph, visited, v):
    queue = deque()
    queue.append(v)
    visited[v] = True

    while queue:
        value = queue.popleft()
        print(value, end=" ")
        for i in graph[value]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


dfs(graph, visit, v)
visit = [False] * (n+1)
print()
bfs(graph, visit, v)