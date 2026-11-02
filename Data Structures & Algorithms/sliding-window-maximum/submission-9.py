from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Alt solution:
        # Maintain a list curr where you pop all the elements < the new element
        ## This works because now only the new elem could be the max of
        ## subsequent windows
        # Once you reach kth elem (k-1 index) start noting curr[0] as the max
        ## This works because if any subsequent elem was > curr[0] then ...
        ## it would have been popped out

        curr = deque([])
        ans = []
        n = len(nums)
        
        for i in range(n):
            while curr and nums[curr[-1]] <= nums[i]:
                curr.pop()
            
            curr.append(i)

            if curr[0] <= i - k:
                curr.popleft()
            
            if i >= k - 1:
                ans.append(nums[curr[0]])
        
        return ans
                

        