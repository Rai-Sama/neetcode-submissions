class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for indx, i in enumerate(nums):
            if target - i in seen:
                return [seen[target-i], indx]
            
            seen[i] = indx
            
            
        
        

        