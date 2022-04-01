class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = []
        for idx in range(len(s)):
            l.append(s.pop())
            if len(s) < 1:
                break
        for idx in range(len(l)):
            s.append(l[idx])
            if len(l) < 1:
                break
