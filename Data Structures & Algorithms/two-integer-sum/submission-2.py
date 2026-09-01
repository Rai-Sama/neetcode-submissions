class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        diffs = [target - i for i in nums]
        for i in range(n):
            if diffs[i] in nums[i+1:]:
                return [i, nums[i+1:].index(diffs[i]) + i+1]
