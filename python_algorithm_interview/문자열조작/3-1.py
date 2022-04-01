class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        #문자와 숫자 나눠서 넣기 
        letters, digits = [], []
        for log in logs:
            #첫번째 인덱스는 식별자 
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        #식별자 제외하고 문자열만 정렬 후, 동일하면 후순위로 식별자순으로 정렬
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        #숫자의 경우에는 순서 상관없이 뒤에 그냥 붙이면됨
        return letters + digits
        
'''정렬 우선순위를 람다식에서 , 로 구분하면 가능'''
