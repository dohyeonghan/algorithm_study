'''

카드 합 < 21
카드 합이 최대

양의정수
n장의 카드
숫자 M

n장 중 3장
M을 넘지 않으면서 M과 최대한 가깝게

n : 5 M : 21
5 6 7 8 9

세장을 조합
'''

from itertools import combinations

n, m = map(int, input().split())

for _ in range(n):
