'''
N * M 크기 직사각형
각각 육지 or 바다

바다로는 못감
(A,B) -> A는 북쪽으로부터니까 y축 , B는 x축

현재방향 기준 왼쪽부터 차례대로
안간곳 있으면 가고 아니면 방향만 돌림
바다거나 다가봤으면 방향을 유지하고 한칸뒤로, 뒤쪽도 바다인경우 멈춘다.

입력
세로 크기 N 가로크기 M (3<= <= 50)
캐릭터 있는 좌표 (A,B), 바라보는 방향 d 공백으로 구분하여 주어짐
- 0 : 북쪽
- 1 : 동쪽
- 2 : 남쪽
- 3 : 서쪽
셋째줄에는 육지인지 바다인지
- 0 : 육지
- 1 : 바다
처음 칸은 항상 육지
이동후 방문한 칸의 수를 구함

방향을 설정해서 이동하는 문제 유형에서는 dx, dy를 별도로 만드는 것이 효과적
동서남북 기준으로 숫자 구분하면 되겠다.
파이썬 2차원 리스트 선언시 컴프리헨션 쓰는게 효과적


'''
n, m = map(int, input().split())
# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]

x, y, direction = map(int, input().split())
d[x][y] = 1
# 전체 맵 정보 받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn_left():
    global direction
    # 왼쪽으로
    direction -= 1
    # 한바퀴 다돌면? 서쪽
    if direction == -1:
        direction = 3


count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전 후 정면에 가보지 않은 칸이 있으면 이동
    # d[nx][ny] == 0 은 가본 경우 확인하는 맵
    # array[nx]ny] == 0 은 입력받은 맵, 육지
    # 즉 안가봤고 육지라면 -> 간다.
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전 후 가본지 않은 곳 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 못갈 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있으면 이동
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0
print(count)


