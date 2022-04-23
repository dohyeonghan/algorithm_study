from  itertools import combinations

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
h = []
c = []
C = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            h.append((i,j))
        if graph[i][j] == 2:
            c.append((i,j))
C = list(combinations(c,m))
# print(C)
# print(C[0])
d_sum_list = []
for i in range(len(C)):
    for j in range(m):
        for k in range(len(h)):
            d_sum = 0
            distance = abs(h[k][0]-C[i][j][0]) + abs(h[k][1]-C[i][j][1])
            d_sum += distance
            d_sum_list.append(d_sum)
print(d_sum_list)
# d_list = []
# for i in range(len(h)):
#     for j in range(len(C)):
#         distance = abs(h[i][0]-C[i][0]) + abs(h[i][1]-C[i][1])