class SinglyLinkedList():
    def __init__(self):
        self.data = None
        self.next = None
        self.prev = None

def reverse(head):
    curr = head 
    prev = None 

    while curr:
        next = curr.next 
        prev = curr.prev 
        curr.next = prev 
        curr.prev = next 
        curr = next
    return head 
