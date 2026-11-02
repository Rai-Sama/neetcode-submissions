class MinStack:

    def __init__(self):
        self.stack = []
        self.mn = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.mn and val > self.mn[-1]:
            self.mn.append(self.mn[-1])
        else:
            self.mn.append(val)

    def pop(self) -> None: # No edge cases - guaranteed by the question
        self.stack.pop()
        self.mn.pop()

    def top(self) -> int: # No edge cases - guaranteed by the question
        return self.stack[-1]

    def getMin(self) -> int: # No edge cases - guaranteed by the question
        return self.mn[-1]