# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())

# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))
# 데이터 정렬
data.sort()
# 가장 큰수
first = data[n-1]
# 두번째로 큰수
second = data[n-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1 # 숫자 더해지는 횟수니까 하나씩 줄어듦
    if m == 0:
        break
    result += second
    m -= 1

print(result)