n = int(input())
candidate=[]
for _ in range(n):
    r, data = input().split()
    candidate.append([r,data])
for i in range(len(candidate)):
    answer = ''
    for j in candidate[i][1]:
        answer += j * int(candidate[i][0])
    print(answer)