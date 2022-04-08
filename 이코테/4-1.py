#상하좌우 문제

'''내 풀이
1,1에서 n,n까지
L R U D를 해석해서 좌표로 바꿔주기
입력은 공간크기와 계획서
처음 좌표 (1,1)부터 시작해서
좌표를 x리스트, y리스트로 지정?
if L -> x - 1
if R -> x + 1
if U -> y + 1
if D -> y - 1
1미만 5초과하면 적용안하기
'''

'''해설
1. 시간복잡도 생각 : 이동횟수에 비례 
이동횟수와 연산횟수가 비례 -> O(N)
'''
n = int(input())
x, y = 1, 1
plans = input().split()
# L, R, U, D에 따른 이동방향
# 문제에 따라 달라짐
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L' 'R', 'U', 'D']

#이동 계획을 하나씩 확인
for plan in plans:
    #이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    #공간 벗어나면 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        #조건에 해당하면 다음 루프로
        #pass라면 아무것도 안하지만 continue는 다음 단계
        continue
    x, y = nx, ny

print(x,y)

