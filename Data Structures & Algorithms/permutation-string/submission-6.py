class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)

        if n > m:
            return False
        
        cnts = {}
        for i in s1:
            cnts[i] = cnts.get(i, 0) + 1

        tcnts = cnts.copy()
        i, r = 0, 0

        while r < m:
            if s2[r] in tcnts:
                tcnts[s2[r]] -= 1
                
                if not tcnts[s2[r]]:
                    tcnts.pop(s2[r])
                
                if not tcnts:
                    return True

                r += 1
            else:
                tcnts = cnts.copy()
                i += 1
                r = i
        
        if not tcnts:
            return True
        return False
