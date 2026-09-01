class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = [i for i in s]
        l2 = [i for i in t]
        l1.sort()
        l2.sort()
        if l1 == l2:
            return True
        else:
            return False