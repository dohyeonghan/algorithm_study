from itertools import combinations
import sys
# input = sys.stdin.readline

height = [int(input()) for _ in range(9)]

candidate = list(combinations(height, 2))
for c in candidate:
    if sum(c) == 100:
        ans = list(c)
        break
ans.sort()
for i in ans:
    print(i)