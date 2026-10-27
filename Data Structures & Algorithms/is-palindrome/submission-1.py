class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([i.lower() for i in s if i.isalnum()])
        rev = s[::-1]

        if s == rev:
            return True
        return False