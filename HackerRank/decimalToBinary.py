class Stack():
    def __init__(self):
        self.items = [] 
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop() 

    def is_empty(self):
        return self.items == [] 

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)
        
    def show(self):
        return self.items

def convert2Binary(decimal):
    stack = Stack()
    while decimal!=0:
        stack.push(decimal%2)
        decimal //= 2 
    binary = ""
    while not stack.is_empty():
        binary += str(stack.pop())
    
    return binary 

print(convert2Binary(10))
