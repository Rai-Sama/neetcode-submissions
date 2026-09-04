class MinStack:

    def __init__(self):
        self.stack = []
        self.mn = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.mn):
            self.mn.append(min(self.mn[-1], val))
        else:
            self.mn.append(val)

    def pop(self) -> None:
        self.stack = self.stack[:-1]
        self.mn = self.mn[:-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mn[-1]
