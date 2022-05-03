numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = 'right'

def solution(numbers, hand):
    answer = ''
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [-1, 0, -2]]
    # 왼손 오른손 위치
    left = []
    right = []
    for num in numbers:
        if num in [1,4,7]:
            answer + 'L'

        if num in [3,6,9]:
            answer + 'R'
    return answer

