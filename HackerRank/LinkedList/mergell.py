class SinglyLinkedList():
    def __init__(self,data,next):
        self.data = data  
        self.next = next 
    
for t in range(int(input())):

    n = int(input("1st ll: "))
    head1 = SinglyLinkedList(int(input()),None)  
    prev = head1 
    for i in range(n-1):
        data = int(input())
        newNode = SinglyLinkedList(data,None) 
        prev.next = newNode
        prev = prev.next 
    
    n = int(input("2nd ll: "))
    head2 = SinglyLinkedList(int(input()),None)  
    prev = head2
    for i in range(n-1):
        data = int(input())
        newNode = SinglyLinkedList(data,None) 
        prev.next = newNode
        prev = prev.next 
    curr1,curr2 = head1,head2
    dummy = SinglyLinkedList(None,None)
    curr = dummy
   
    while True:
        if curr1 is None:
            curr.next = curr2 
            break 
            
        if curr2 is None :
            curr.next = curr1
            break 

        newNode = SinglyLinkedList(None,None)
        if curr1.data < curr2.data:
            newNode.data = curr1.data 
            curr1 = curr1.next 
            curr.next = newNode 
        else:
            newNode.data = curr2.data 
            curr2 = curr2.next 
            curr.next = newNode
        curr = curr.next 
    
    
        
    head = dummy.next 
        

    currNode = head 
    while not (currNode is None):
        print(currNode.data)
        currNode = currNode.next
        
                 


    
        


    
     
        
    
    



        



        
    