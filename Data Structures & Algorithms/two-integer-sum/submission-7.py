class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cnts = {}
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in cnts:
                return [i, cnts[diff]]
            else:
                cnts[nums[i]] = i
            
        
        

        