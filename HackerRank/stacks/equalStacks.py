

#Recursive solution
# def equalStack(sum1,stack1,sum2,stack2,sum3,stack3):
#     if sum1==sum2==sum3:
#         return sum1
#     elif sum1==0 or sum2 ==0 or sum3 == 0:
#         return 0
#     else:
#         minimum = min(sum1,sum2,sum3)
        
#         while sum1 > minimum and len(stack1):
#             sum1 -= stack1.pop(0)
#         while sum2 > minimum and len(stack2):
#             sum2 -= stack2.pop(0)
#         while sum3 > minimum and len(stack3):
#             sum3 -= stack3.pop(0)
        
#         return equalStack(sum1,stack1,sum2,stack2,sum3,stack3)

def equalStacks(h1,h2,h3):
    def equalStackHelper(h1,s1,h2,s2,h3,s3):
        while not(s1==s2==s3):
            if s1 == max(s1,s2,s3):
                s1 -= h1.pop(0)
            elif s2 == max(s1,s2,s3):
                s2 -= h2.pop(0)
            elif s3 == max(s1,s2,s3):
                s3 -= h3.pop(0)

        return s1 
    return equalStackHelper(h1,sum(h1),h2,sum(h2),h3,sum(h3))



h1,h2,h3 = map(int,input().split())
stack1 = list(map(int, input().split()))
stack2 = list(map(int, input().split()))
stack3 = list(map(int, input().split()))
print(equalStack(sum(stack1),stack1,sum(stack2),stack2,sum(stack3),stack3)) 
        
        
            

