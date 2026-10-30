class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        maps = {'(': ')', '{': '}', '[': ']'}
        for i in s:
            if i in maps:
                stack.append(i)
            else:
                if not stack:
                    return False
                if maps.get(stack.pop(), False) != i:
                    return False
        if not stack:
            return True
        return False
