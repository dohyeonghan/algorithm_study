k = []

for _ in range(9):
  n = int(input())
  k.append(n)

k.sort()
from itertools import combinations
for i in combinations(k,7):
  sum = 0
  for idx in range(len(i)):
    sum += i[idx]
  if sum == 100:
    for j in i:
      print(j)
    break
