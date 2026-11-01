import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # l, r = 0, k-1 (no edge case: k is bounded by n)
        # Maintain a max heap of size k
        # At each step (till r < n):
        ## Remove nums[l] and add nums[r+1] to the heap
        ## Add max element in the heap (heap[0]) to ans
        # Return the ans list

        n = len(nums)
        l, r = 0, k-1

        mxhp = [(nums[i], i) for i in range(k)]
        #mnhp = [(nums[i], i) for i in range(k)]
        els = set([i for i in mxhp])
        heapq.heapify_max(mxhp)
        #heapq.heapify(mnhp)
        ans = [mxhp[0]]
        
        while r < n-1:
            r += 1
            l += 1
            while mxhp and mxhp[0][1] < l:
                heapq.heappop_max(mxhp)
            #while mnhp and mnhp[0][1] < l:
            #    heapq.heappop(mnhp)
            
            heapq.heappush_max(mxhp, (nums[r], r))
            #heapq.heappush(mnhp, nums[r])

            ans.append(mxhp[0])

        return [i[0] for i in ans]