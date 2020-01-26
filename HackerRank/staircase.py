def staircase(n):
    for i in range(n):
        for j in range(n-1,i,-1):
            print(" ", end = "")
        for j in range(i+1):
            print("#", end = "")
            
        print()
staircase(6)

    #
   ##
  ###
 ####
#####
    
