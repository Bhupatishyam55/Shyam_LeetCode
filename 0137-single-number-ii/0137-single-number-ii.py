class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x = Counter(nums)
        for k,v in x.items():
            if v!=3:
                return k