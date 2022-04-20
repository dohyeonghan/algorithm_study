from collections import deque

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True

    while queue:
        v = queue.popleft()
        print(v, end= ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


bfs(graph, 1, visited)

'''
bfs는 재귀 아니고
deque 사용
처음 노드로 queue 만든다
queue가 빈 것이 아닌동안 
이전 v를 빼고 popleft
인접 노드들이 방문하지 않은 거면 전부 집어넣는다. 

끝나면 다음 루프로 가서 popleft하고 순서대로 넣었으니까 바로 다음 노드 
다음 노드에 넘어가서 똑같이 반복
'''