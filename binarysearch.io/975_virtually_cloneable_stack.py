class VirtuallyCloneableStacks:
    def __init__(self):
        self.stack = [0,]

    def copyPush(self, i):
        self.stack.append(self.stack[i] + 1)
        
    def copyPop(self, i):
        self.stack.append(self.stack[i] -1)

    def size(self, i):
        return self.stack[i]