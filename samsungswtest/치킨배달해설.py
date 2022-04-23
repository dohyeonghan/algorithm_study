from itertools import combinations

n, m = map(int, input().split())
chicken, house = [], []

for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r,c))
        elif data[c] == 2:
            chicken.append((r,c))

candidates = list(combinations(chicken,m))

def get_sum(candidate):
    result = 0
    for hx, hy in house:
        temp = 9999999
        for cx, cy in candidate:
            temp = min(temp, abs(hx-cx) + abs(hy-cy))
        result += temp

result = 9999999
for candidate in candidates:
    result = get_sum(candidate)

print(result)