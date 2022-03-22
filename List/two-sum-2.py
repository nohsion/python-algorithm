# https://leetcode.com/problems/two-sum
# 투 포인터 이용 - 인덱스가 아닌 값을 찾아내는 문제에만 적용 가능
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    nums.sort()
    left, right = 0, len(nums)-1
    while not left == right:
        if nums[left] + nums[right] < target:
            left += 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [nums[left], nums[right]]

print(twoSum([2, 15, 11, 7], 22))

# result = [['a', 'b'], ['a', 'b'], ['b', 'a'], ['c', 'd']]
# new_result = list(set(map(tuple, result)))
# new_result = list(set([tuple(set(item)) for item in result]))
# print(new_result)