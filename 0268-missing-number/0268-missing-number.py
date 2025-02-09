class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        lst=list(range(n+1))
        for i in range(len(lst)):
            if lst[i] not in nums:
                return lst[i]