from itertools import combinations

n , m = map(int,input().split())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
house = []
chicken = []
for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            house.append((i,j))
        if data[i][j] == 2:
            chicken.append((i,j))

candidates = list(combinations(chicken,m))
result_candidate = []
for candidate in candidates:
    chic_dist = []
    for h in house:
        temp = []
        for c in candidate:
            # 한 집당 치킨거리
            dist = abs(h[0]-c[0]) + abs(h[1]-c[1])
            temp.append(dist)

        chic_dist.append(min(temp))
    result_candidate.append(sum(chic_dist))

print(min(result_candidate))
