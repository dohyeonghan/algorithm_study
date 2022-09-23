def solution(s):
    answer = len(s)
    for step in range(1,len(s)//2+1):
        cnt = 1
        res = ''
        prev = s[0:step]
        for j in range(step, len(s), step):
            # print(j)
            if prev == s[j:j+step]:
                cnt += 1
            else:
                if cnt == 1:
                    res += prev
                else:
                    res += str(cnt) + prev
                    # res += prev
                prev = s[j:j+step]
                cnt = 1
        # print('처리전')
        # print(res)
        # 다돌고 같아서 카운트만 증가시키고 for문 끝난 경우
        if cnt == 1:
            res += prev
        else:
            res += str(cnt) + prev
        # res += prev
        # print('처리후')
        # print(res)
        answer = min(answer, len(res))
    return answer
