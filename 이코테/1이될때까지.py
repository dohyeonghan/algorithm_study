# n, k = map(int, input().split())
# count = 0
# print(n,k)
# while True:
#     if n == 1:
#         break
#     else:
#         if n % k == 0:
#             n %= k
#             count += 1
#
#         else:
#             n -= 1
#             count += 1
#
# print(count)

n, k = map(int, input().split())
result = 0

while n >= k: #두 변수 나눌때 주의점
    while n % k != 0:
        n-= 1
        result += 1
    n //= k # 나머지가 아니라 몫인것
    result += 1

print(result)