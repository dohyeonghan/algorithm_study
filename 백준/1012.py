import sys
t = int(input())
input = sys.stdin.readline().rstrip()
def dfs(x,y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False
result = []
for _ in range(t):
    cnt = 0
    n, m, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1
    for i in range(n):
        for j in range(m):
            if dfs(i,j):
                cnt += 1
    result.append(cnt)
for i in range(len(result)):
    print(result[i])

