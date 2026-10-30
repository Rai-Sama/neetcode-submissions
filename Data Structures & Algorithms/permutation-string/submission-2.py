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
        for i in s2:
            if i in tcnts:
                tcnts[i] -= 1
                if not tcnts[i]:
                    tcnts.pop(i)
                if not tcnts:
                    return True
            else:
                tcnts = cnts.copy()
        return False
