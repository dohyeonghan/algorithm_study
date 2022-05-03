class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]
        # 예외처리 : s 길이가 2보다 짧거나 s자체가 팰린드롬일때
        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''
        # 슬라이딩 윈도우 오른쪽으로 이동
        for i in range(len(s)-1):
            result = max(result, expand(i,i+1), expand(i,i+2), key=len)

        return result