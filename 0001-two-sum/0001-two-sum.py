class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dect={}
        for  i , n in enumerate(nums):
            res=target-n
            if res in dect:
                return [dect[res],i]
            dect[n]=i
