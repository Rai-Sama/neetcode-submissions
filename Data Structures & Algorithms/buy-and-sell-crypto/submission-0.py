class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        mn = prices[0]

        for i in prices:
            p = max(p, i - mn)
            mn = min(i, mn)
        
        return p