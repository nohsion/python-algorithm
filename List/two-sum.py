# https://leetcode.com/problems/two-sum
from typing import List

# 0. 내 풀이 (3362 ms)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for idx, tn in enumerate(nums):
            tt = target - tn
            for i in range(idx + 1, len(nums)):
                if tt == nums[i]:
                    result.append(idx)
                    result.append(i)
                    return result

# 1. 내 풀이와 비슷한데, in을 이용! (672 ms)
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, n in enumerate(nums):
            complement = target - n

            # 이 방법을 몰라서 위에서 for문을 씀 ㅜㅜ
            if complement in nums[idx+1:]:
                # idx = nums.index(n)
                return [idx, nums[idx+1:].index(complement) + (idx+1)]

# 2. 딕셔너리 - 첫 번째 수를 뺀 결과 key 조회 (56 ms)
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        # key와 value를 바꿔서 딕셔너리로 저장
        for i, num in enumerate(nums):
            nums_map[num] = i

        # 타겟에서 첫 번째 수를 뺀 결과를 key로 조회
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return [i, nums_map[target - num]]

# 3. 2번 풀이 개선 (간결한 코드) (56 ms)
class Solution3:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [i, nums_map[target-num]]
            nums_map[num] = i