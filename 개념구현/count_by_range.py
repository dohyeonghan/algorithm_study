from bisect import bisect_left, bisect_right
'''
bisect는 정렬된 객체내에서 같은 값들이 여러개 있으면
제일 처음 인덱스와 제일 마지막 인덱스를 확인할 수 있음
-> 같은 값들이 몇개 있는지, 어디에 있는지 확인할 수 있음

left_value와 right_value를 받았을때
그 사이에 몇개가 있는지 확인하는 count_by_range함수'''
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

a = [1,2,3,3,3,3,4,4,8,9]
# 값이 4인 데이터 개수 출력
print(count_by_range(a,4,4))
# 값이 [-1,3] 범위에 있는 데이터 개수 출력
print(count_by_range(a,-1,3))