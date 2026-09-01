class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n1 = len(s)
        n2 = len(t)
        if n1 != n2:
            return False
        cnt1 = {}
        cnt2 = {}

        for i in range(n1):
            if s[i] in cnt1:
                cnt1[s[i]] += 1
            else:
                cnt1[s[i]] = 1

            if t[i] in cnt2:
                cnt2[t[i]] += 1
            else:
                cnt2[t[i]] = 1
        
        if cnt1 == cnt2:
            return True
        else:
            return False
