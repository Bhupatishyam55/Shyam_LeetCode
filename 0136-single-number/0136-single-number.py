from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x = Counter(nums)
        for k,v in x.items():
            if v==1:
                return k
        