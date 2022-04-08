from collections import deque
'''큐 구현시 deque를 이용해서 append와 popleft 함수를 사용하면
들어오는 순서대로 나갈 수 있다.'''
data = deque([2,3,4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data))