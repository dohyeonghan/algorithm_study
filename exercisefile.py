paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

# print(paragraph.split())
# print(paragraph.lower().split())
from collections import defaultdict
import re
words = []
print(re.sub(r'[^\w]', ' ', paragraph).lower().split())
# [] 빼먹지 않고 넣기
# r -> raw 문자열 : 백슬래쉬가 많이 쓰이는 정규식에서 활용
# 공백인지 아무것도 없는건지 잘 확인하기 -> 아무것도 없이 하니 전체 단어가 붙어버림
# 리스트에 .lower()해도 전체 값에 대해 lower 처리됨
for word in re.sub(r'[^\w]', ' ', paragraph).lower().split():
    if word not in banned:
        words.append(word)
# defaultdict로 초기화 안해도 되게끔

counts = defaultdict(int)
for word in words:
    counts[word] += 1

print(counts)
# max 함수, key는 counts.get -> argmax의 역할(max를 만들게 하는 x)을 할 수 있도록
'''
.get(key)해서 해당 키에 대한 값을 출력해주는 함수. 
키를 입력으로 value를 출력하기 때문에 value 최댓값을 기준으로 하여 key를 출력해줌.
'''
print(max(counts, key=counts.get))

'''카운트 객체 이용하기'''
from collections import Counter

counter = Counter(words)
print(counter.most_common(1)[0][0])
