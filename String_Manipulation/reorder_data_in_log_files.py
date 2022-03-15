# https://leetcode.com/problems/reorder-data-in-log-files/
from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        digits = []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        # 문자(x.split()[1:])를 첫 번째 우선순위로 하고, 식별자(x.split()[0])를 두 번째 우선순위로 하여 정렬
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        return letters + digits
