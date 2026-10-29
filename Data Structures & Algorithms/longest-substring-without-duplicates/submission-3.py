class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cnts = {} # char: indx
        mx = 0
        l, r = 0, 0
        n = len(s)
        while r < n:
            curr = s[r]
            if curr in cnts:
                l = cnts[curr] + 1
                cnts[curr] = r
            else:
                cnts[curr] = r
            mx = max(mx, r - l + 1)
            r += 1
        
        return mx
            