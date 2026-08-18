class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        #Output[i] = nums[nums[i]]
        ans = []
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        return ans
        