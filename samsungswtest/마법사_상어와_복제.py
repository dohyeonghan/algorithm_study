import copy

f_dx = [0,-1,-1,-1,0,1,1,1]
f_dy = [-1,-1,0,1,1,1,0,-1]
dx = [-1,0,1,0]
dy = [0,-1,0,1]

m,s = map(int, input().split())
fish = [list(map(int, input().split())) for _ in range(m)]
graph = [[[] for _ in range(4)] for _ in range(4)]

for x, y, d in fish:
    # 좌표 주의
    graph[x-1][y-1].append(d-1)

shark = tuple(map(lambda x: int(x) -1, input().split()))
smell = [[0] * 4 for _ in range(4)]

for _ in range(s):
    eat = list()
    max_eat = -1
    # 1. 모든 물고기 복제
    temp = copy.deepcopy(graph)
    # 2. 물고기 이동
    temp = move_fish()
    # 3. 상어 이동 - 백트래킹
    dfs(shark[0], shark[1], 0,0,list())
    for x, y in eat:
        if temp[x][y]:
            temp[x][y] = []
            smell[x][y] = 3 # 3번 돌아야 없어짐
    # 4. 냄새 사라짐
    for i in range(4):
        for j in range(4):
            if smell[i][j]:
                smell[i][j] -= 1
    # 5. 복제 마법
    for i in range(4):
        for j in range(4):
            graph[i][j] += temp[i][j]
answer = 0
for i in range(4):
    for j in range(4):
        answer += len(graph[i][j])

print(answer)

def move_fish():
    '''물고기 이동
    1. 상어 있고 물고기 냄새 있고 벗어나는 칸 x
    2. 45도 반시계 회전 후 이동, 이동 못하면 그대로
    '''

    # 3차원 리스트 맵, 물고기 정보
    res = [[[] for _ in range(4)] for _ in range(4)]
    for x in range(4):
        for y in range(4):
            while temp[x][y]:
                d = temp[x][y].pop()
                for i in range(d, d-8, -1):
                    i %= 8
                    nx, ny = x + f_dx[i], y + f_dy[i]
                    if (nx,ny) != shark and 0<= nx < 4 and 0 <= ny < 4 and not smell[nx][ny]:
                        res[nx][ny].append(i)
                        break
                else:
                    res[x][y].append(d)
    return res

def dfs(x,y, dep, cnt, visit):
    '''
    상어 3칸 이동
    1. 제외되는 물고기 수가 많고 > 이동방법 사전순(백트래킹하면 자동으로 됨)
    2. 이동한 곳을 저장 > 물고기 냄새가 됨
    :param x:
    :param y:
    :param dep:
    :param cnt:
    :param visit:
    :return:
    '''
    global max_eat, shark, eat
    if dep == 3:
        if max_eat < cnt:
            max_eat = cnt
            shark = (x,y)
            eat = visit[:]
        return
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < 4 and 0 <= ny < 4:
            if (nx, ny) not in visit:
                # 처음 방문, 카운트에 죽은 물고기 수 추가
                visit.append((nx,ny))
                dfs(nx, ny, dep + 1, cnt + len(temp[nx][ny]), visit)
                visit.pop()
            else:
                # 방문한 경우
                dfs(nx, ny, dep + 1, cnt, visit)

