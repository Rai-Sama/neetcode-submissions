class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rev = nums[::-1]
        pref = [1]
        n = len(nums)
        # T(n) = O(n)
        for i in range(1, n):
            pref.append(pref[i-1]*nums[i-1])
        
        
        post = [1]
        for i in range(1, n):
            post.append(post[i-1]*rev[i-1])
        

        res = []
        for i in range(n):
            res.append(pref[i] * post[n - 1 - i])
        
        return res
