class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        '''데이터 전처리
        정규식에서 \w -> word character
        ^ -> not 
        word char가 아닌 모든 문자를 공백으로 치환
        
        '''
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
        #값을 자동으로 int로 초기화
        counts = collections.defaultdict(int)
        for word in words:
            counts[word] += 1
        
        return max(counts, key=counts.get)
        
        
