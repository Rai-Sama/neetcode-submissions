class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)

        if n < m:
            return ""


        l = 0
        rem, start = m, 0
        cnts = {}
        for i in t:
            cnts[i] = cnts.get(i, 0) + 1
        
        mn = 10**5+1

        for r in range(n):
            if s[r] in cnts:
                if cnts[s[r]] > 0:
                    rem -= 1
                
                cnts[s[r]] -= 1
            
            while rem == 0: # substring is valid
                if r - l + 1 < mn:
                    mn = r - l + 1
                    start = l
                
                if s[l] in cnts:
                    cnts[s[l]] += 1
                    if cnts[s[l]] > 0:
                        rem += 1
                
                l += 1
        
        return s[start:start+mn] if mn < 10**5+1 else ""
            