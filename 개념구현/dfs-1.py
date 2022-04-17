def dfs(graph, v, visited):
    # 방문 다했으면 pop
    visited[v] = True
    # 한줄로 표현하기 위해 end 공백 사용
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
'''

인덱스랑 통일하기 위해 0 인덱스도 추가해줌 
1 - 2,3,8
2- 1,7
3-1,4,5
4-3,5
5-3,4
6-7
7-2,6,8
8-1,7

'''
# 연결 정보를 담은 2차원 리스트
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
# 방문 기록을 담은 리스트
visited = [False] * 9

dfs(graph, 1 , visited)
