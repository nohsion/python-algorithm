# https://leetcode.com/problems/group-anagrams/
from typing import List
import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        for str in strs:
            # 정렬하여 defaultdict에 추가
            anagrams[''.join(sorted(str))].append(str)

        return list(anagrams.values())  # values만 보여주는데, list로 변환해줘야 함