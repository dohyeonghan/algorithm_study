# word = input()
# alphabet = list(range(97,123))  # 아스키코드 숫자 범위
#
# for x in alphabet:
#     print(word.find(chr(x)), end=' ')

data = input()
alpha = 'abcdefghijklmnopqrstuvwxyz'

for item in alpha:
    if item in data:
        print(data.index(item), end = ' ')
    else:
        print(-1, end = ' ')
