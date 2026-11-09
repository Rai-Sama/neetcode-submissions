class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = sorted(s)
        l2 = sorted(t)

        return l1 == l2