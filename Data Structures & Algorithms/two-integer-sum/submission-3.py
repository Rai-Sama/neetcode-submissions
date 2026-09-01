class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        dct = {}
        for i in range(n):
            diff = target - nums[i]
            if diff in dct:
                return [dct[diff], i]
            else:
                dct[nums[i]] = i
