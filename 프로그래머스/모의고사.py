'''
1번 수포자 : 5개
2번 수포자 : 8개
3번 수포자 : 10개

answers : 정답
return : 가장 많이 맞춘 사람
answers 최대 10000

수도코드
answers 돌기
1번은 5개씩
2번은 8개씩
3번은 10개씩

1번 -> answers 돌면서
인덱스 % 5 한다음 1번과비교후
카운트

카운트 세개 넣고 비교 후
제일 큰것

근데 같으면?
max = -1
처음부터 체크
max보다 크면 max로
max와 같으면 result
끝까지 가서 같은거 없으면
max 리턴
같은거 있으면 동일한거 출력
'''
answers = [1, 2, 3, 4, 5]

one = [1, 2, 3, 4, 5]
two = [2, 1, 2, 3, 2, 4, 2, 5]
three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]


def solution(answers):
    answer = []
    result1 = 0
    result2 = 0
    result3 = 0

    for i in answers:

        if answers[i%5] == one[i%5]:
            result1 += 1
    for i in answers:
        if answers[i%8] == two[i%8]:
            result2 += 1
    for i in answers:
        if answers[i%10] == three[i%10]:
            result3 += 1
    print(result1,result2,result3)
    return answer
print(solution(answers))