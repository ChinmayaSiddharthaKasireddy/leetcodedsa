class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [-1] * n
        stack = []
        for index in range(0,2*n):
            i = index % n
            while stack and nums[stack[-1]] < nums[i]:
                prev_index = stack.pop()
                result[prev_index]=nums[i]
            if index < n:
                stack.append(i)
        return result

        