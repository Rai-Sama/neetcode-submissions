class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rev = nums[::-1]
        pref = [1]
        for i in range(1, len(nums)):
            pref.append(pref[i-1]*nums[i-1])
        
        
        post = [1]
        for i in range(1, len(rev)):
            post.append(post[i-1]*rev[i-1])
        

        res = []
        for i in range(len(pref)):
            res.append(pref[i] * post[len(post) - 1 - i])
        
        return res
