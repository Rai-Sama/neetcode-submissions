class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closers = {")": "(", "}": "{", "]": "["}
        for i in s:
            if i in closers:
                if len(stack):
                    opener = stack.pop()
                    if opener != closers[i]:
                        return False
                else:
                    return False
            else:
                stack.append(i)
        if len(stack):
            return False
        else:
            return True