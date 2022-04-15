'''
문제 설명 및 초기 아이디어)
N * M
뽑으려는 카드가 있는 행 선태
가장 숫자 낮은 카드 뽑기
처음에 뺄때 가장 낮은 것을 뽑을 걸 고려해서 전략 세워야함

입력
3 3
3 1 2
4 1 4
2 2 2

입력 3 * 3 -> map(int로)
3 1 2
4 1 4
2 2 2 -> 2차원 리스트로

for문 행별로 돌고
각 행을 열별로 돌기
그중에 제일 작은 것 고르고
고른것 빈리스트에 넣고
그중에 제일 큰값 출력

해설)
아이디어 : 각 행마다 가장 작은 수를 찾은 뒤 그 수 중에서 가장 큰 수를 찾는 것
메소드 : min()함수나 2중 반복문

'''

n,m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    # 나는 빈 리스트 할당을 생각했는데 이런 방법도 있음
    result = max(result, min_value)

print(result)

