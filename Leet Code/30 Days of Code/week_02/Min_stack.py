class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minstack = []
        
    def push(self, x: int) -> None:
        if not len(self.minstack) or x <= self.minstack[-1]:
            self.minstack.append(x)
        self.stack.append(x)

    def pop(self) -> None:
        relement = self.stack.pop()
        if relement == self.minstack[-1]:
            self.minstack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
        
