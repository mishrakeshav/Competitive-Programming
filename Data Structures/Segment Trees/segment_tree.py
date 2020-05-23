def build(a):
    """
    builds a segment tree from given array \n
    Input: a - array\n
    Output: t - segment tree\n
    """
    t = [None]*(4*len(a))
    def buildHelper(v,tl,tr):
        if tl==tr:
            t[v] = a[tl]
        else:
            tm = (tl+tr)//2
            buildHelper(v*2+1,tl,tm)
            buildHelper(v*2+2,tm+1,tr)
            t[v] = min(t[v*2+1],t[v*2+2]) 
    buildHelper(0,0,len(a)-1)
    return t 

def sum_queries(a,t,l,r):
    """
    Input:\n
     Takes 4 Parameters,\n
        a: original array
        t: segment tree (array)
        l: lower limit (inclusive)
        r: upper limit (inclusive)
    Ouput:\n
        returns the sum of element in range l to r 
    """
    def Helper(tl,tr,l,r,v):
        if l>r:
            return 0 
        elif l==tl and r==tr:
            return t[v]
        else:
            tm = (tl+tr)//2 
            return Helper(tl,tm,l,min(r,tm),2*v+1) + Helper(tm+1,tr,max(l,tm+1),r,2*v+2)
    return Helper(0,len(a)-1,l,r,0)

def update(a,t,position,new_value):
    
    def Helper(v,tl,tr):
        if tl==tr:
            t[v] = new_value 
        else:
            tm = (tl+tr)//2 
            if position<=tm:
                Helper(2*v+1,tl,tm) 
            else:
                Helper(2*v+2,tm+1,tr)
            t[v] = t[2*v+1] + t[2*v+2]
            
    Helper(0,0,len(a)-1)

a = [1,2,3,4,5,6,7,8,9,10]
t= build(a)
print(t)
print(sum_queries(a,t,0,4))
update(a,t,0,10)
print(sum_queries(a,t,0,4))
