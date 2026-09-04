class Solution:
    def climbStairs(self, n: int) -> int:
        # RECURSION PRACTICE - NOT TRYING TO GET THE OPTIMAL (DP) SOLUTION FOR NOW
        if n <= 2:
            return n
        
        return self.climbStairs(n-1) + self.climbStairs(n-2)