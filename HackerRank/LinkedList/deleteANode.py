class Node():
    def __init__(self,data,next):
        self.data = data 
        self.next = next 

def deleteNode(head, position):
    if head == None:
        return None 
    elif position==0:
        head = head.next
        return head 
    else:
        count = 0
        prev = head 
        iterate = head 
        while count!=position:
            count += 1 
            prev = iterate
            iterate = iterate.next 

        prev.next = iterate.next 
        return head 
n = int(input("Enter number of elements: "))
head = Node(None,None)
iterate = head
for i in range(n):
    iterate.data = int(input("Enter data: "))
    newNode = Node(None,None)
    iterate.next = newNode
    iterate = iterate.next 
p = int(input("Enter the position of the node to delete: "))
head = deleteNode(head,p)
for i in range(n-1):
    print(head.data,"->", end = " ")
    head = head.next

    