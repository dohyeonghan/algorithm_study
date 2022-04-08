from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])
print(counter['green'])
#카운터 객체를 딕셔너리로 변환
print(dict(counter))