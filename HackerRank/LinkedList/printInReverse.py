class Node():
    def __init__(self,data,next):
        self.data = data 
        self.next = next 
def reversePrint(head):
    if head!=None:
        iterate = head 
        reversePrint(head.next)
        print(head.data)
        

