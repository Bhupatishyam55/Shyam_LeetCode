class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x = Counter(nums)
        return [k for k,v in x.items() if v == 1]