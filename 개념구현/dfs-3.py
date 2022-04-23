'''
인접행렬로 구현하기

'''
adj = [[0] * 13 for _ in range(13)]

def dfs(now):
    for nxt in range(13):
        if adj[now][nxt]:
            dfs(nxt)

dfs(0)