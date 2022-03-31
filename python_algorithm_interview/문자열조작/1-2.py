class Solution:
    # 반환값이 bool값
    def isPalindrome(self, s: str) -> bool:
        # strs = []
        # 리스트 대신 deque를 사용하면 훨씬 빨라진다.
        strs: Deque = collections.deque()
            
        for char in s:
            # 문자열이 알파벳([a-zA-Z])과 숫자([0-9])로만 구성되었는지 확인하는 메소드 
            if char.isalnum():
                # 소문자로 통일해서 strs 빈리스트에 차례대로 넣어준다.
                strs.append(char.lower())
        
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False 
        
        return True 
        
        
            
        
