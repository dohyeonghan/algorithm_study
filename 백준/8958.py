n = int(input())
tfs = []
result = []
for _ in range(n):
    tfs.append(input())
for items in tfs:
    score = 0
    sum_score = 0
    for item in items:
        if item == 'O':
            score += 1
            sum_score += score
        else:
            score = 0
    print(sum_score)