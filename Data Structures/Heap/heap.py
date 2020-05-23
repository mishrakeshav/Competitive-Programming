##############################################################
        ###########-----MAX HEAP-----############
##############################################################
#top to bottom approach 
def max_heapify(A,i,size):
    l = 2*i +1
    r = 2*i +2
    largest = i 
    if(l < size and A[l] > A[largest]):
        largest = l 
    
    if(r < size and A[r] > A[largest]):
        largest = r 
    if largest != i:
        A[largest],A[i] = A[i],A[largest]
        max_heapify(A,largest,size)
#bottom to up approach
def max_heapify_bu(heap,i):
    parent = (i-1)//2 
    if parent >= 0 and  heap[i] > heap[parent]:
        heap[i],heap[parent] = heap[parent],heap[i]
        max_heapify_bu(heap,parent)

def build_max_heap(A):
    n = len(A)
    for i in range(n//2,-1,-1):
        max_heapify(A,i,n)

def heapSort(A):
    n = len(A) -1
    build_max_heap(A)
    while n>=0:
        A[0],A[n]=A[n],A[0]
        max_heapify(A,0,n)
        n -= 1 

def getMaximum(heap):
    return heap[0]

def extractMax(heap):
    maximum = heap[0]
    heap[0] = heap[-1]
    heap.pop()
    max_heapify(heap,0,len(A))
    return maximum

def deleteElementMaxHeap(heap,element):
    for i in range(len(heap)):
        if element == heap[i]:
            heap[i] = heap[-1]
            heap.pop() 
            max_heapify(heap,i,len(heap)) 
            return True 
    return False 

def insertElementMaxHeap(heap,element):
    heap.append(element)
    max_heapify_bu(heap,len(heap)-1) 

##############################################################
        ###########-----MIN HEAP-----############
##############################################################
def min_heapify(A,i,size):
    l = 2*i +1
    r = 2*i +2
    smallest = i 
    if(l < size and A[l] < A[smallest]):
        smallest = l 
    
    if(r < size and A[r] < A[smallest]):
        smallest = r 
    if smallest != i:
        A[smallest],A[i] = A[i],A[smallest]
        min_heapify(A,smallest,size)

def build_min_heap(A):
    n = len(A)
    for i in range(n//2,-1,-1):
        min_heapify(A,i,n)

def getMinimum(heap):
    return heap[0]

def extractMin(heap):
    maximum = heap[0]
    heap[0] = heap[-1]
    heap.pop()
    min_heapify(heap,0,len(A))
    return maximum

def deleteElementMinHeap(heap,element):
    for i in range(len(heap)):
        if element == heap[i]:
            heap[i] = heap[-1]
            heap.pop() 
            min_heapify(heap,i,len(heap)) 
            return True 
    return False

def min_heapify_bu(heap,i):
    parent = (i-1)//2 
    if parent >= 0 and  heap[i] < heap[parent]:
        heap[i],heap[parent] = heap[parent],heap[i]
        min_heapify_bu(heap,parent) 

def insertElementMinHeap(heap,element):
    heap.append(element)
    min_heapify_bu(heap,len(heap)-1) 



A = [1, 9, 10, 8, 6, 25, 19, 20, 22, 21,100,101,0,89]
build_min_heap(A)
print(A)
insertElementMinHeap(A,-1)
print(A)
deleteElementMinHeap(A,-1)
print(A)
print(extractMin(A))
print(A)