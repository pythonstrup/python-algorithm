n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):

    if x < 0 or y < 0 or x > n-1 or y > n-1:
        return False

    if graph[x][y] == 1:
        global number
        graph[x][y] = 0
        number += 1

        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True

    return False

number = 0
complex = 0
result = []

for i in range(n):
    for j in range(n):
        if dfs(i, j):
            complex += 1
            result.append(number)
            number = 0

result.sort()
print(complex)
for i in range(complex):
    print(result[i])