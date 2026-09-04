class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        
        q2 = deque()
        while len(self.q) > 1:
            q2.append(self.q.popleft())
        

        val = self.q.popleft()
        self.q = q2
        
        return val

    def top(self) -> int:
        print("Checking top of ", self.q)
        q2 = deque()
        while len(self.q) > 1:
            q2.append(self.q.popleft())
                
        val = self.q[0]
        self.q = q2 + self.q
      
        return val
        
    def empty(self) -> bool:
        if len(self.q):
            return False
        else:
            return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()