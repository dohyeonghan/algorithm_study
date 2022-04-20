'''
재귀함수는 스택과 같다고 생각하면 쉽다.
마지막 호출된 함수가 끝나야 그전 함수가 끝나고
최종적으로 처음에 호출된 함수가 끝난다.
'''

def recursive_function(i):
    if i == 100:
        return
    print(i, '번째 재귀함수에서', i+1, '번째 재귀함수를'
                               '호출합니다.')
    recursive_function(i+1)
    print(i, '번째 재귀함수를 종료합니다.')

recursive_function(1)

