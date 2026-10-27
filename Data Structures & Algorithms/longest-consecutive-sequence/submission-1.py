class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cnts = {}
        mx = 0
        for i in nums:
            if i - 1 in cnts:
                cnts[i] = max(cnts[i-1] + 1, cnts.get(i, 1))
            else:
                cnts[i] = cnts.get(i, 1)
                
            mx = max(mx, cnts[i])
            j = i + 1
            while j in cnts:
                cnts[j] = max(cnts[j-1] + 1, cnts[j])
                mx = max(mx, cnts[j])
                j += 1

        return mx
