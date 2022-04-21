input_data = input()
alpha = []
sum = 0

for item in input_data:
    if item.isdigit():
        sum += int(item)
    else:
        alpha.append(item)

alpha.sort()
print(''.join(alpha)+ str(sum))