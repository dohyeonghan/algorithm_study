from collections import deque

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        strs = deque()
        for char in s:
            if char.isalnum():
                strs.append(char)
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        return True
