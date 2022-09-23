# n = 8
# k = 2
# cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
# cmds = []
# a.insert(a,b) : a 인덱스에 b 삽입
def solution(n, k, cmd):
    cmds=[]
    answer = ''
    before_data = [i for i in range(n)]
    after_data = before_data.copy()
    deleted = []
    check = k
    for item in cmd:
        cmds.append(item.split())
    for i in range(len(cmds)):
        if cmds[i][0] == 'D':
            check += int(cmds[i][1])
        if cmds[i][0] == 'U':
            check -= int(cmds[i][1])
        if cmds[i][0] == 'C':
            if check == len(after_data)-1:
                deleted.append([check, after_data[check]])
                del after_data[check]
                check -= 1
            else:
                deleted.append([check, after_data[check]])
                del after_data[check]
            # check는 자동으로 내려감
        if cmd[i][0] == 'Z':
            index, d = deleted.pop()
            after_data.insert(index, d)
            check += 1
    for i in range(len(before_data)):
        if before_data[i] in after_data:
            answer += 'O'
        else:
            answer += 'X'
    return answer
#
# print(solution(n,k,cmd))