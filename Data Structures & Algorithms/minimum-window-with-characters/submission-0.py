class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)

        if n < m:
            return ""


        l, r = 0, 0
        cnts = {}
        for i in t:
            cnts[i] = cnts.get(i, 0) + 1
        
        mn = (10**5+1, "")
        tcnts = cnts.copy()
        while r < n:
            if s[r] in tcnts:
                tcnts[s[r]] -= 1

                if tcnts[s[r]] <= 0:
                    tcnts.pop(s[r])

                
            elif tcnts:
                r += 1
            
            if not tcnts:
                mn = (r-l+1, s[l:r+1]) if (r - l + 1) < mn[0] else mn
                if s[l] in cnts:
                    tcnts[s[l]] = 1
                l += 1
        
        return mn[1]
            