class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        b=int(''.join(map(str,digits)))
        b+=1
        return list(map(int,str(b)))
        