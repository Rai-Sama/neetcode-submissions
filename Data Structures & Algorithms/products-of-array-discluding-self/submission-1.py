class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        cnt = 0
        res = []
        pos = -1
        for i in range(len(nums)):
            if nums[i]:
                prod *= nums[i]
            else:
                cnt += 1
                pos = i
        if cnt > 1:
            return [0] * (len(nums))
        elif cnt == 1:
            return [0 if i != pos else prod for i in range(len(nums))]
        
        return [prod//i for i in nums]
