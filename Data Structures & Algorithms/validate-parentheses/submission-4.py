class Solution:
    def isValid(self, s: str) -> bool:
        maps = {"(": ")", "{":"}", "[": "]"}
        stack = []

        for i in s:
            if i in maps:
                stack.append(i)
            else:
                if not stack or maps[stack.pop()] != i:
                    return False

            return len(stack) == 0
