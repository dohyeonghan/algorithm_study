from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            # sorted는 리스트 반환
            anagrams[''.join(sorted(s))].append(s)
        return list(anagrams.values())