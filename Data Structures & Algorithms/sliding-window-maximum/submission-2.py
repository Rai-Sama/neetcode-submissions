import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # l, r = 0, k-1 (no edge case: k is bounded by n)
        # Maintain a max heap of size k
        # At each step (till r < n):
        ## Keep removing the max element if ...
        ## it isn't in the new window (i < l+1) the  and add nums[r+1] to the heap
        ## Add max element in the heap (heap[0]) to ans
        # Return the ans list

        n = len(nums)
        l, r = 0, k-1

        mxhp = [(nums[i], i) for i in range(k)]

        heapq.heapify_max(mxhp)

        ans = [mxhp[0]]
        
        while r < n-1:
            r += 1
            l += 1
            while mxhp and mxhp[0][1] < l:
                heapq.heappop_max(mxhp)
            
            heapq.heappush_max(mxhp, (nums[r], r))

            ans.append(mxhp[0])

        return [i[0] for i in ans]