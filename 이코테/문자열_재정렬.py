'''
K1KA5CB7 입력시
ABCKK13 출력
'''
import time
input_data = input()
start = time.time()


alpha = []
sum = 0
for item in input_data:
    if item.isalpha():
        alpha.append(item)
    else:
        sum += int(item)
alpha.sort()

print(''.join(alpha) + str(sum))
print("time :", time.time() - start)

'''join 

'구분자'.join(리스트) 

'''
