class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None: # No edge cases - guaranteed by the question
        self.stack.pop()

    def top(self) -> int: # No edge cases - guaranteed by the question
        return self.stack[-1]

    def getMin(self) -> int: # No edge cases - guaranteed by the question
        mn = self.stack[0]
        for i in self.stack[1:]:
            mn = min(mn, i)
        return mn