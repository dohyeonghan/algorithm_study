N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins.reverse()
ans = 0
for coin in coins:
    ans += K // coin
    K %= coin
    print(f'coin: {coin}, K: {K}, ans: {ans}') # 중간 점검!
print(ans)