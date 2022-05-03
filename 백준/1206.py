'''bfs dfs 구현 '''

# n 정점 , m 간선 , v 시작점

n, m ,v = map(int, input().split())

# 인접행렬로 만들기 -> 노드만 주어졌을때
graph = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

from collections import deque
def bfs(start_v):
    discovered = [start_v]
    q = deque()
    q.append(start_v)
    while q:
        v = q.popleft()
        print(v, end=' ')
        # 행렬이니까 인덱스로 체크
        for w in range(len(graph[start_v])):
            if graph[v][w] == 1 and w not in discovered:
                discovered.append(w)
                q.append(w)

def dfs(start_v, discovered=[]):
    discovered.append(start_v)
    print(start_v, end=' ')
    for w in range(len(graph[start_v])):
        if w not in discovered and graph[start_v][w] == 1:
            dfs(w, discovered)

dfs(v)
print()
bfs(v)

