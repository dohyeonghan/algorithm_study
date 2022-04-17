'''
N종류 개수 제한 없음
합이 K
필요한 동전 개수의 최솟값
입력
N K (N:1-10, K : 1-100000000)

동전의 가치 Ai : 1-1000000 -> 배수

배수인건 입력 받을 때 체크되니까 신경x

'''

n, k = map(int, input().split())
data = []
for _ in range(n):
    data.append(int(input()))
data.sort(reverse=True)
count = 0
for coin in data:
    count += k // coin
    k %= coin

print(count)
