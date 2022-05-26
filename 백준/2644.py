from collections import deque
n = int(input())
one, two = map(int, input().split())
k = int(input())
# a,b 사이의 거리 -> bfs
data = [[]  for _ in range(n+1)]

for _ in range(k):
  a,b = map(int, input().split())
  data[a].append(b)
  data[b].append(a)

visited = [0]*(n+1)

def bfs(node):
  q = deque()
  q.append(node)
  while q:
    node = q.popleft()
    for i in data[node]:
      if visited[i] == 0:
        visited[i] = visited[node] + 1
        q.append(i)

bfs(one)
print(visited[two] if visited[two] > 0 else -1)
