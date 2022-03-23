# https://leetcode.com/problems/product-of-array-except-self/

# 1. 내 풀이 (Time Exceeded 실패)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def front(k):
            result = 1
            for i in range(k):
                result *= nums[i]
            return result

        def rear(k):
            result = 1
            for i in range(len(nums)-1, k, -1):
                result *= nums[i]
            return result

        output = []
        for i in range(len(nums)):
            if i == 0:
                output.append(rear(i))
            elif i == len(nums)-1:
                output.append(front(i))
            else:
                output.append(rear(i)*front(i))

        return output

# 2. 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈 (380 ms)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []

        # 왼쪽 곱셈
        p = 1
        for i in range(0, len(nums)):
            out.append(p)
            p *= nums[i]

        # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
        p = 1
        for i in range(len(nums)-1, 0-1, -1):
            out[i] *= p
            p *= nums[i]

        return out
