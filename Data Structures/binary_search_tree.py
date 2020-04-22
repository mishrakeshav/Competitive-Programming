class Node():
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None 


def insert(root,val):
    if root is None:
        return Node(val)
    elif val < root.val:
        root.left = insert(root.left,val)
    elif val > root.val:
        root.right = insert(root.right, val)
    return root

def insert_iterative(root,val):
    newnode = Node(val)

    curr = root
    prev = None

    while curr != None:
        prev = curr
        if curr.val > val:
            curr = curr.left 
        elif curr.val < val:
            curr = curr.right

    if prev is None:
        return newnode
    elif prev.val > val:
        prev.left = newnode
    else:
        prev.right = newnode

    return root

def smallest(root):
    curr = root
    while curr.left is not None:
        curr = curr.left
    return curr


def delete(root,val):
    if root is None:
        return root
    if val < root.val:
        # val is less than root.val
        root.left = delete(root.left, val)
    elif val > root.val:
        # val is greater than root.val
        root.right = delete(root.right, val)
    else:
        # val is equal to root.val
        if root.left is None and root.right is None:
            #Node is Leaf
            root = None
        elif root.right is None:
            #Node has only left child
            root = root.left
        elif root.left is None:
            #Node has only right child
            root = root.right
        else:
            smallest_node = smallest(root.right)
            root.val = smallest.val
            root.right = delete(root.right,smallest.val)
    return root


def search(root,val):
    if root is None:
        return False 
    if root.val == val:
        return True 
    if val < root.val:
        return search(root.left,val)
    if val > root.val:
        return search(root.right, val)
    
def search_iterative(root,val):
    while root != None:
        if root.val > val:
            root = root.left 
        elif root.val < val:
            root = root.right
        else:
            return True
    return False


def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.val,end = " ")
    inorder(root.right)

def preorder(root):
    if root is None:
        return
    print(root.val, end = " ")
    preorder(root.left)
    preorder(root.right)

def postorder(root):
    if root is None:
        return
    preorder(root.left)
    preorder(root.right)
    print(root.val, end = " ")





root = insert(None,5)
root = insert(root,4)
root = insert(root,15)
root = insert(root,6)
root = insert(root,14)
root = insert(root,7)
root = insert(root,13)
root = insert(root,8)
root = insert(root,12)
root = insert(root,9)
root = insert(root,11)
root = insert(root,10)
root = insert(root,0)
root = insert(root,100)
root = insert(root,-5)
root = insert(root,88)
root = insert(root,90)


inorder(root)
print("\n")


root = delete(root,12)

inorder(root)
print("\n")


 

    


    


