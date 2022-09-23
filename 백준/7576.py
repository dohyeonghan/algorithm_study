'''bfs로 체크
결과값 변수 -> max 찾기
bfs -> 초반에 1인 값들에 대하여, bfs 돌고 나면 전체 다돎
-> 즉 다음 칸에는 날짜를 넣음으로써 며칠 지났는지 확인 가능
-> 아직 남아있는 1값에 대해서만 돌리기
-> 다돌았는데 0이 하나라도 있다? -> exit
-> 마지막 확인때는 그냥 한줄씩만 확인해도 됨
->
'''
from collections import deque
m,n = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

q = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i,j))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
res = 0
def bfs():
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx,ny))

bfs()
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))
print(res-1)








