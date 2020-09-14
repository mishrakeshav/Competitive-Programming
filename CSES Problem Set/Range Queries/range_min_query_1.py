
def build(segment_tree,a,l,r,i):
    if l == r:
        segment_tree[i] = a[l]
    else:
        m = (l+r)//2 
        build(segment_tree,a,l,m,2*i+1)
        build(segment_tree,a,m+1,r,2*i+2)
        segment_tree[i] = min(segment_tree[2*i+1] ,segment_tree[2*i+2])
    return segment_tree

def query(segment_tree,tl,tr,l,r,i):
    if l > r:
        return float('inf')
    if tl == l and tr == r:
        return segment_tree[i]
    else:
        tm = (tl+tr)//2 
        left = query(segment_tree,tl,tm,l,min(tm,r),2*i+1)
        right = query(segment_tree,tm+1,tr, max(l,tm+1), r,2*i+2)
        return  min(left , right)

def update(segment_tree, index,l,r,value,i):
    if l == r :
        segment_tree[i] = value 
    else:
        m = (l+r)//2 
        if(index <= m):
            update(segment_tree,index,l,m,value,2*i+1)
        else:
            update(segment_tree,index,m+1,r,value,2*i+2)
        segment_tree[i] = min(segment_tree[2*i+1] , segment_tree[2*i+2])
  

if __name__ == '__main__':
    n,q = map(int, input().split())
    a = list(map(int, input().split()))
    segment_tree = [None for i in range(4*n+1)]
    build(segment_tree,a,0,n-1,0)
    # Query for Updation
    # for i in range(q):
    #     idx,value = map(int,input().split())
    #     update(segment_tree, idx,0,n-1,value,0)
    #     print(segment_tree)               
    print(segment_tree)
    # Range Queries
    for i in range(q):
        l,r = map(int, input().split())
        ans = query(segment_tree,0,n-1,l-1,r-1,0)
        print(ans)


