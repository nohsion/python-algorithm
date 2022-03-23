# https://leetcode.com/problems/array-partition-i

# 1. 내 풀이 (짝수 번째 값만 계산)
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        for i in range(0, len(nums), 2):
            result += nums[i]
        return result

# 2. 파이썬다운 방식
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
