# computers = int(input())
# net = int(input())
# graph = [[0] * (computers + 1) for _ in range(computers+1)]
# data = [list(map(int, input().split())) for _ in range(net)]
# for item in data:
#     graph[item[0]][item[1]] = graph[item[1]][item[0]] = 1
# # print(graph)
# def dfs(i,j):
#     global count
#     if i <= 0 or i > computers or j <= 0 or j > computers:
#         return False
#     if graph[i][j] == 1:
#         graph[i][j] = 0
#         count += 1
#         dfs(i-1,j)
#         dfs(i+1,j)
#         dfs(i,j-1)
#         dfs(i,j+1)
#         return True
#     return False
# count = 0
# # for i in range(1,computers+1):
# #     for j in range(1,computers+1):
# #         if dfs(i,j) == True:
# #             count += 1
# dfs(1,2)
# print(count)

n = int(input())
m = int(input())

graph =