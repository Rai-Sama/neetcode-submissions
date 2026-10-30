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
        i = 0
        while i < m:
            while i < m and s2[i] in tcnts:
                tcnts[s2[i]] -= 1
                if not tcnts[s2[i]]:
                    tcnts.pop(s2[i])
                if not tcnts:
                    return True
                i += 1
            if i < m and s2[i] not in tcnts:
                tcnts = cnts.copy()
            i += 1
        return False
