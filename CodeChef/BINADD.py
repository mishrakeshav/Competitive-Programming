# Brute Force Approach
def add(a,b):
    count = 0
    while b > 0:
        U = a^b 
        V = a & b 
        a = U 
        b = V<<1
        count += 1 
    print(count)
    print(a)
     
# add(0,100010)
# add(1,1)
# add(1,0)
# add(0,1)
# add(00,1)
# add(00,10)
# add(00,11)
# add(1,1)
# add(1,10)
# add(1,11)
# add(10,1)
# add(10,10)
# add(10,11)
# add(11,1)
# add(11,10)
# add(11,11)

# add(47,51) #5

#sum is 2^n - 1
# add(4,11)  #1
# add(8,7)   #1
# add(15,16)  #1

#numbers are powers of 2 but not equal
# add(2,4)  #1
# add(8,4)  #1

#numbers are equal   #2
#add(7,7)
#add(128,128)
add(56,56)
add(18,18)
