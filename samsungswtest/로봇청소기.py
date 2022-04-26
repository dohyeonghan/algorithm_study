n, m = map(int, input().split())

r, c, d = map(int, input().split())

default_map = []

for i in range(n):
    default_map.append(list(map(int, input().split())))

clean_map = [[0] * m for i in range(n)]

r, c = 1, 1
clean_count = 1
clean_map[r][c] = 1
direction = 0
turn_count = 0

def turn_left(direction):
    direction -= 1
    if direction == -1:
        direction = 3
    return direction

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

while True:
    direction = turn_left(direction)
    # turn_count += 1
    nr = r + dr[direction]
    nc = c + dc[direction]

    if clean_map[nr][nc] == 0 and default_map[nr][nc] == 0:
        clean_map[nr][nc] = 1
        r = nr
        n = nc
        clean_count += 1
        turn_count = 0
        continue
    else:
        turn_count += 1

    if turn_count == 4:
        nr = r - dr[direction]
        nc = c - dc[direction]
        if default_map[nr][nc] == 0:
            r = nr
            c = nc
            turn_count = 0
        else:
            turn_count = 0
            break

print(clean_count)


