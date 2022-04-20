input_data = input()
'''
input_data[0] -> column
input_data[1] -> row
'''

row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-1,2), (1,2), (-2,1), (-2,-1), (-1,-2), (1,-2),(2,1),(2,-1)]
count = 0

for i in range(len(steps)):
    nrow = row + steps[i][0]
    ncolumn = column + steps[i][1]
    if nrow < 1 or ncolumn < 1 or nrow > 8 or ncolumn >8:
        continue
    else:
        count += 1

print(count)
