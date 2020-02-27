class SinglyLinkedList():
    def __init__(self,data,next):
        self.data = data  
        self.next = next 
    
for t in range(int(input())):

    n = int(input())
    head1 = SinglyLinkedList(int(input()),None)  
    prev = head1 
    for i in range(n-1):
        data = int(input())
        newNode = SinglyLinkedList(data,None) 
        prev.next = newNode
        prev = prev.next 
    
    n = int(input())
    head2 = SinglyLinkedList(int(input()),None)  
    prev = head2
    for i in range(n-1):
        data = int(input())
        newNode = SinglyLinkedList(data,None) 
        prev.next = newNode
        prev = prev.next 
    curr1,curr2 = head1,head2
    if curr1==None and curr1 == None:
        print(1)
    elif curr1== None or curr2 == None:
        print(0)
    while True :
        if curr1==None and curr1 == None:
            print(1)
            break
        elif curr1== None or curr2 == None:
            print(0)
        if(curr1.data != curr2.data):
            print(0)
            break 
        curr1 = curr1.next
        curr2 = curr2.next 
    
    
        


    
     
        
    
    



        



        
    