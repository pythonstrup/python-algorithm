from collections import deque

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [1, 0]
dy = [0, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    visit = [[False]*n for _ in range(n)]

    while queue:
        x, y = queue.popleft()
        move = graph[x][y]

        if move == -1:
            return True

        for i in range(2):
            nx = x + dx[i]*move
            ny = y + dy[i] * move

            if 0 <= nx < n and 0 <= ny < n:
                if not visit[nx][ny]:
                    visit[nx][ny] = True
                    queue.append((nx, ny))

if bfs(0, 0):
    print("HaruHaru")
else:
    print("Hing")