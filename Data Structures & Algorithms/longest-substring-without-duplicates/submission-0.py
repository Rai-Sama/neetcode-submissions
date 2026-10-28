class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mx = 0
        n = len(s)
        i = 0
        curr = 0
        unq = set()
        while i < n:
            if s[i] in unq:
                unq = set()
                unq.add(s[i])
                curr = 1
            
            else:
                unq.add(s[i])
                curr += 1
            i += 1
            mx = max(curr, mx)

        return mx
        