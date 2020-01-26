#Python implementation of stack
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


def matches(open,close):
    opens = "([{"
    closes = ")]}"
    return opens.index(open) == closes.index(close)


def parenthesesChecker(string):
    balanced = True 
    index = 0
    symbol = ""
    stack = Stack()
    while index < len(string) and balanced:

        symbol = string[index]
        # print(symbol)
        if symbol in "([{":
            stack.push(symbol)
            # print(stack.show())
        else:
            # print(stack.peek())
            if stack.is_empty():
                balanced = False
            elif matches(stack.peek(), symbol):
                stack.pop() 
            else:
                balanced = False 
        index += 1 
    if balanced and stack.is_empty():
        return True 
    else:
        return False

print(parenthesesChecker("{[()]}"))
print(parenthesesChecker("{[(])}"))
print(parenthesesChecker("{{[[(())]]}}"))
                
            


        

    