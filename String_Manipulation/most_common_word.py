# https://leetcode.com/problems/most-common-word
from typing import List
import re
from collections import defaultdict
from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
            .lower().split()
                 if word not in banned]

        counts = defaultdict(int)
        for word in words:
            counts[word] += 1
        # max에 key를 지정해 counts에서 값이 가장 큰 키를 가져옴
        return max(counts, key=counts.get)


class Solution1:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
            .lower().split()
                 if word not in banned]

        counts = Counter(words)
        # 가장 흔하게 등장하는 단어의 첫 번째 인덱스 리턴
        return counts.most_common(1)[0][0]
