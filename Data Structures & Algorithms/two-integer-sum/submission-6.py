class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = [target - i for i in nums]
        cnts = {}
        for i in range(len(nums)):
            if nums[i] in cnts:
                cnts[nums[i]].append(i)
            else:
                cnts[nums[i]] = [i]
        
        for i in range(len(diffs)):
            if diffs[i] in cnts:
                if diffs[i] == nums[i] and len(cnts[nums[i]]) > 1:
                    return [i, cnts[nums[i]][1]]
                elif diffs[i] in cnts:
                    return [i, cnts[diffs[i]][0]]
        