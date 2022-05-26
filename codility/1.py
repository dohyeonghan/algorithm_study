# N = 1041
#
# def solution(N):
#     # write your code in Python 3.6
#     binary = bin(N)
#     binary = binary[2:].split('1')
#     # print(binary)
#     result = []
#     for item in binary:
#         result.append(len(item))
#     # print(result[-1])
#     if result[-1] != 0:
#         return max(result[:-1])
#     else:
#         return max(result)
#
# print(solution(N))

a = format(1024, 'b')
print(type(a))