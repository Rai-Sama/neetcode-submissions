class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cnts = {}
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in cnts:
                return [cnts[diff], i]
            else:
                cnts[nums[i]] = i
            
        
        

        