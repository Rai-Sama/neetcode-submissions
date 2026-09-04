def climb(n):
    if n == 2:
        return 2
    if n == 1:
        return 1
    return climb(n-1) + climb(n-2)

class Solution:
    def climbStairs(self, n: int) -> int:
        return climb(n)