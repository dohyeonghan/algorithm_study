n = int(input())

plan = input().split()

dx = [0,0,-1,1]
dy = [-1,1,0,0]
type = ['L', 'R', 'U', 'D']
x,y = 1,1

for i in range(len(plan)):
    for j in range(len(type)):
        if plan[i] == type[j]:
            nx = x + dx[j]
            ny = y + dy[j]
            if nx < 1 or ny < 1 or nx > n or ny > n:
                continue
            else:
                x = nx
                y = ny

print('(',x,',',y,')')

