class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        curr = []
        mx = 0
        l = 0
        for i in s:
            try:
                indx = curr.index(i)
                curr = curr[indx + 1:]
                curr.append(i)
                l = len(curr)
            except:
                curr.append(i)
                l += 1

            mx = max(mx, l)

        return mx
            