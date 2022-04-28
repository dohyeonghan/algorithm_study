from collections import deque

n, m = map(int, input().split())
# graph = []
# for _ in range(n):
#     graph.append(list(map(int, input().split())))
graph = [list(map(int, input().split())) for _ in range(n)]

# 구름좌표 : 튜플말고 리스트로!! & 좌표니까 -1씩
cloud = deque([[n-1, 0], [n-1, 1], [n - 2, 0], [n - 2, 1]])
# print(cloud)
# a, b = cloud.popleft()
# print(a,b)
# info = []
# # 이동정보 info 방향, 거리
# # [[1, 3], [3, 4], [8, 1], [4, 8]]
# for _ in range(m):
#     info.append(list(map(int, input().split())))
info = [list(map(int, input().split())) for _ in range(m)]
# print(info)

#방향정보
dr = [0,-1,-1,-1,0,1,1,1]
dc = [-1,-1,0,1,1,1,0,-1]

# 이동 m번동안 비바라기 시작
for i in range(m):
    # 이동
    # 구름 좌표 돌면서 방향대로 계산
    for j in range(len(cloud)):
        r = cloud[j][0]
        c = cloud[j][1]
        for _ in range(info[i][1]):
            # 한칸이동
            nr = r + dr[info[i][0] - 1]
            nc = c + dc[info[i][0] - 1]
            # 경계값 넘어갈때
            if nr == -1:
                nr = n-1
            if nc == -1:
                nc = n-1
            if nr == n:
                nr = 0
            if nc == n:
                nc = 0
            # 구름좌표 바꿔주기
            cloud[j][0] = nr
            cloud[j][1] = nc
            # 다음 루프 넘어가도록 처리해주기
            r = nr
            c = nc
    # print(cloud)
    # 비내리기 : 구름좌표 돌면서 그래프 좌표값에 물 + 1씩 넣기
    for j in range(len(cloud)):
        r = cloud[j][0]
        c = cloud[j][1]
        graph[r][c] += 1

    # 구름 사라지기
    discarded = cloud
    # print(discarded)
    # print(discarded)
    # 기존 클라우드 비워주기
    cloud = []
    # print(discarded)
    # 물복사
    # 물이 증가한 칸 = discarded 좌표
    for j in range(len(discarded)):
        cnt = 0
        for k in range(4):
            r = discarded[j][0]
            c = discarded[j][1]
            # print(r,c)
            v = 2 * k + 1
            # print(v)
            nr = r + dr[v]
            # print(nr)
            nc = c + dc[v]
            # print(nc)
            if nr >= 0 and nr <= n-1 and nc >= 0 and nc <= n-1:
                if graph[nr][nc] > 0:
                    cnt += 1
        graph[r][c] += cnt


    # 다시 구름 생기기
    for j in range(n):
        for k in range(n):
            # 모든 그래프에서 물이 2이상이고 버렸던 구름칸이 아닐때
            if graph[j][k] >= 2:
                if [j,k] not in discarded:
                    # 해당 칸에 모두 구름 반영
                    cloud.append([j,k])
                    graph[j][k] -= 2
result = 0
for i in range(n):
    for j in range(n):
        result += graph[i][j]

print(result)



