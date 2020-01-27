def powersum(target,power,num = 1):

    if num**power < target :
        return powersum(target,power,num = num+1) + powersum(target-num**power,power,num+1)
    elif num**power == target:
        return 1 
    else:
        return 0
print(powersum(100,2))

