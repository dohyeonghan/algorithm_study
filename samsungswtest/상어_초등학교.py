n = int(input())

graph = [[0] * n for _ in range(n)] # 좌표 0부터 시작

# 학생 정보 입력
students = [list(map(int, input().split())) for _ in range(n**2)]

# print(students)

# 상하좌우 방향 입력
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# n**2명의 학생들을 돌면서 프로그램 시작

for student in students:
    # print(student)
    # 각 학생들 좌표별로 정보 넣고 그중에서 정렬해서 최종 결과값에 넣어야함
    # print(student[1:])
    temp_info = []
    # 한 학생이 가진 정보 student -> 리스트 형태로 학생, 좋아하는 네명 순서
    for i in range(n):
        for j in range(n):
            # 각 칸별로 zero 개수, like 개수 구해야함
            if graph[i][j] == 0:
                zero = 0
                like = 0
                for k in range(4):
                    nr = i + dr[k]
                    nc = j + dc[k]
                    # print(nr, nc)
                    # 벽으로 나가면? 고려 안해도됨
                    if 0 <= nr < n and 0 <= nc < n:
                        if graph[nr][nc] == 0:
                            zero += 1
                        # 인접 노드에 좋아하는 학생이 있는 경우
                        elif graph[nr][nc] in student[1:]:
                            like += 1
                # 네방향 다돌았으면 각각 좌표에 대한 정보 넣어주기
                temp_info.append([like, zero, i, j])
    # print(temp_info)
    # 전체 좌표 다돌았으면 temp_info에서 최상의 결과 꺼내야함
    # 정렬은 sort 함수에 람다식 넣어서 like, zero는 내림차순, i, j는 오름차순으로 해야함
    temp_info = sorted(temp_info, key=lambda x: (-x[0], -x[1], x[2], x[3]))

    # print(temp_info)
    # print(temp_info)
    # 정렬후 제일 첫번째 값을 꺼내고 그 좌표를 맵에 저장
        # 그래프의 좌표에 학생 정보 첫번째 자기자신 값을 넣어줌
    graph[temp_info[0][2]][temp_info[0][3]] = student[0]

# print(graph)
# print(graph)
# 학생정보의 값을 정렬해버리면 학생 번호 순서대로 접근할 수 있음
students.sort()
# print(students)
# 각 학생별로 저장이 끝났으면 점수 넣어줘야함
result = 0

for i in range(n):
    for j in range(n):
        # 각 칸별로 점수 매김
        cnt = 0
        for k in range(4):
            nr = i + dr[k]
            nc = j + dc[k]
            if 0 <= nr < n and 0 <= nc < n:
                if graph[nr][nc] in students[graph[i][j]-1]:
                    cnt += 1
        # 네방향 다 돌았으면 점수 계산
        if cnt != 0:
            num = 10 ** (cnt - 1)
            result += num
print(result)