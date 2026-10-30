class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        mx = 1 # 1 since s.length is in [1, 10^5]
        cnts = {} # Frequencies

        for r, x in enumerate(s):
            
            cnts[x] = cnts.get(x, 0) + 1

            while (r - l + 1) - max(cnts.values()) > k: # shorten the window from the left till it becomes valid
                cnts[s[l]] -= 1
                l += 1
            
            mx = max(mx, r - l + 1)
        
        return mx
            
