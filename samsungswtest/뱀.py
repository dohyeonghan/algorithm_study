n = int(input()) # 맵
k = int(input()) # 사과 개수

graph = [[0] * (n+1) for _ in range(n+1)]

for _ in range(k):
    a, b = map(int, input().split())
    graph[a][b] = 1

info = [] # 방향 변화 데이터
L = int(input())
for _ in range(L):
    x, c = input().split()
    info.append((int(x), c))

x, y = 1, 1
graph[x][y] = 2 # 뱀의 위치
direction = 0 # 동 0 남 1 서 2 북 3
# 동, 남, 서, 북 방향
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
q = [(x,y)] # 뱀의 위치 좌표 모음
time = 0
index = 0
while True:
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 다음 위치에 사과가 없다면 꼬리는 비우고 머리만
    if graph[nx][ny] == 0:
        # 머리
        graph[nx][ny] = 2
        # 꼬리 비우기 1. 뱀위치에서 2. 그래프에서
        px, py = q.pop(0)
        graph[px][py] = 0
        # 새로운 위치 정보 등록
        q.append((nx,ny))
        # 새로운 현재 뱀 머리 등록
        x = nx
        y = ny
        time += 1

    # 사과가 있는 경우, 이경우 꼬리와 머리 둘다 2
    if graph[nx][ny] == 1:
        graph[nx][ny] = 2

        q. append((nx,ny))

        x = nx
        y = ny

        time += 1

    # 뱀이 자기자신을 만났을 경우 시간 추가하고 끝
    if graph[ny][ny] == 2:
        time += 1
        break
    # 맵을 벗어났을 경우
    if nx < 1 or ny < 1 or nx > n or ny > n:
        time += 1
        break

    if index < L:
        if time == info[index][0]:
            if info[index][1] == 'L':
                direction = (direction - 1) % 4
                index += 1

            if info[index][1] == 'D':
                direction = (direction + 1) % 4
                index += 1

print(time)