input_data = input()
sum1 =0
sum2 =0
for i in range(int(len(input_data)/2)):
    sum1 += int(input_data[i])
    sum2 += int(input_data[i+int(len(input_data)/2)])

if sum1 == sum2:
    print('LUCKY')
else:
    print('READY')
