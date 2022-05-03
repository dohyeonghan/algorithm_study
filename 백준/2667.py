n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
num =[]
# print(graph)
# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]
# result_graph = [[0] * n for _ in range(n)]
def dfs(x,y):
    if x < 0 or x >=n or y <0 or y >= n:
        return False

    if graph[x][y] == 1:
        global count
        count += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx,ny)
        return True
    return False

count = 0
result = 0

for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:
            num.append(count)
            result += 1
            count = 0
num.sort()
print(result)
for i in range(len(num)):
    print(num[i])