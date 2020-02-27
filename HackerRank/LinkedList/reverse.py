class SinglyLinkedList():
    def __init__(self,data,next):
        self.data = data  
        self.next = next 
    
for t in range(int(input())):
    n = int(input())
    head = SinglyLinkedList(int(input()),None)  
    prev = head 
    for i in range(n-1):
        data = int(input())
        newNode = SinglyLinkedList(data,None) 
        prev.next = newNode
        prev = prev.next 
    currNode = head 
    while currNode!=None:
        print(currNode.data)
        currNode = currNode.next
    currNode = head 
    prev = None 
    nextNode = None 
    
    while currNode!=None:
        nextNode = currNode.next 
        currNode.next = prev 
        prev = currNode 
        currNode = nextNode 
     
        
    head = prev
    currNode = head
    while currNode!=None:
        print(currNode.data)
        currNode = currNode.next



        



        
    