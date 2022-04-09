n = input()
'''
dx dy 구하고
수평 두칸 수직 한칸
수직 두칸 수평 한칸

x축은 숫자로 바꾸는게 편한가

왼쪽 위아래 -> x - 2, y +- 1
오른쪽 위아래 -> x + 2, y +- 1
위 왼오른 -> x +- 1, y + 2
아래 왼오른 -> x +- 1, y - 2
'''
x = n[0]
y = int(n[1])

x_set = ['a','b','c','d','e','f','g','h']


for i in range(len(x_set)):
    if x == x_set[i]:
        x = i + 1

dx = [-2, -2, 2, 2, -1, 1, -1, 1]
dy = [-1, 1, -1, 1, 2, 2, -2, -2]
count = 0

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > 8 or nx > 8:
        continue
    else:
        count += 1
print(count)

