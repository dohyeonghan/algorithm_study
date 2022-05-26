# '''
# 친구의 친구까지만 초대가 가능
# 1번(상근이)를 시작으로 너비우선탐색, 거리(dist)가 2이하인 노드들만
# '''
# import sys
# from collections import defaultdict, deque
#
# def bfs(start):
#     cnt = 0
#     visited = [0 for _ in range(n+1)]
#     visited[start] = 1
#     queue = deque([[start, 0]])
#     while queue:
#         u, dist = queue.popleft()
#         if dist <= 2:
#             cnt += 1
#         for v in g[u]:
#             if not visited[v]:
#                 visited[v] = 1
#                 queue.append([v,dist+1])
#     return cnt - 1 # cnt에 본인도 포함되어 있으므로
#
# n = int(sys.stdin.readline().strip())
# m = int(sys.stdin.readline().strip())
# g = defaultdict(list)
# for _ in range(m):
#     a, b = map(int, sys.stdin.readline().split())
#     g[a].append(b)
#     g[b].append(a)
#
# print(bfs(1))

