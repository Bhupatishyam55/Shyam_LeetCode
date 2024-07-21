class Solution:
    def isValid(self, s: str) -> bool:
        stc=[]
        dec={
            '(':')',
            '{':'}',
            '[':']',
        }
        for i in s:
            if i in dec:
                stc.append(i);
            elif len(stc)==0 or i!=dec[stc.pop()]:
                return False
        return len(stc)==0
        
