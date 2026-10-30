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
        last = -1
        while i < m:
            if s2[i] in tcnts:
                tcnts[s2[i]] -= 1
                if not tcnts[s2[i]]:
                    tcnts.pop(s2[i])
                if not tcnts:
                    return True
                last = i
                i += 1
            else:
                tcnts = cnts.copy()
                i = last + 1 if last >= 0 else i + 1
                last = -1
        return False
