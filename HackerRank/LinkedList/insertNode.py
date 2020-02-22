class Node():
    def __init__(self,data,next):
        self.data = data 
        self.next = next
def insertNodeAtPosition(head, data, position):
    newNode = Node(data,None)
    if head == None:
        return newNode 
    elif position==0:
        newNode.next = head 
        head = newNode
        return head 
    else:
        count = 0
        prev = head 
        iterate = head 
        while count!=position:
            count += 1 
            prev = iterate
            iterate = iterate.next 
        newNode.next = iterate
        prev.next = newNode 
        return head
