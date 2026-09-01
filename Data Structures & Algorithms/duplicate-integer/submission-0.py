class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cnts = {}
        for i in nums:
            if i in cnts:
                return True
            else:
                cnts[i] = 1
        return False