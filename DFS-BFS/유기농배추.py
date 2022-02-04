
t = int(input())

def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True

    return False

for test in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]

    for i in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j):
                cnt += 1

    print(cnt)

