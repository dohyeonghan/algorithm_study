from collections import Counter
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = []
        for word in re.sub(r'[^\w]', ' ', paragraph).split():
            word = word.lower()
            if word not in banned:
                words.append(word)

        counts = Counter(words)
        return counts.most_common(1)[0][0]

