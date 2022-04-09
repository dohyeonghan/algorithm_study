'''
n = 0 -> 1사이클
n이 3의 배수
n은 0-23까지
range 조심
시간을 합쳐서 str으로 만들기
'''

n = int(input())
count = 0
for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h)+str(m)+str(s):
                count += 1
print(count)

