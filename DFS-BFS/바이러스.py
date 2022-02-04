
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

visit = [False] * (n+1)
count = 0

def dfs(graph, visited, v):
    global count
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            count += 1
            dfs(graph, visited, i)



dfs(graph, visit, 1)
print(count)