class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        m=len(nums)
        nums=set(nums)
        for i in range(1,m+1):
            if i not in nums:
                return i
        return max(nums)+1