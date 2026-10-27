class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hshmp = {}
        for indx, i in enumerate(nums):
            if target - i in hshmp:
                return [hshmp[target-i], indx]
            
            hshmp[i] = indx
            
        
        

        