class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_c=[amount+1]*(amount+1)
        min_c[0]=0
        for i in range(1,amount+1):
            for c in coins:
                if i-c>=0:
                    min_c[i]=min(min_c[i],1+min_c[i-c])
        return min_c[-1] if min_c[-1]!= amount+1 else -1