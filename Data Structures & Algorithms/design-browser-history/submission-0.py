class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.curr = 0

    def visit(self, url: str) -> None:
        self.curr += 1
        self.history = self.history[:self.curr] + [url]

    def back(self, steps: int) -> str:

        while self.curr and steps:
            steps -= 1
            self.curr -= 1
        
        return self.history[self.curr]

    def forward(self, steps: int) -> str:
        
        while self.curr < len(self.history)-1 and steps:
            self.curr += 1
            steps -= 1
        
        return self.history[self.curr]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)