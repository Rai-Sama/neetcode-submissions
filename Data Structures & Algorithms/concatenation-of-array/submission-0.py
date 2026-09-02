class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [i for i in nums]
        ans.extend(ans)
        return ans