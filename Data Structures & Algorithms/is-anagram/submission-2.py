class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnts = {}
        for i in s:
            if i in cnts:
                cnts[i] += 1
            else:
                cnts[i] = 1
        
        for i in t:
            if i in cnts:
                cnts[i] -= 1
            else:
                return False
        for i in cnts.keys():
            if cnts[i]:
                return False
        return True