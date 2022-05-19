from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

dist = [-1] * (n + 1)
dist[x] = 0

# print(graph)
# print(dist)
q = deque([x])
while q:
    i = q.popleft()
    for j in graph[i]:
        if dist[j] == -1:
            q.append(j)
            dist[j] = dist[i] + 1
# print(dist)
check = False
for i in range(1, n + 1):
    if dist[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)
