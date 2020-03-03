stack = []
maximum = [-999999999,-9999999999]
maximum_element = -99999999
for q in range(int(input())):
    commands = list(map(int, input().split()))
    if commands[0]==1:
        if commands[1] >= maximum_element:
            maximum_element = commands[1]
            maximum.append(maximum_element)

        stack.append(commands[1])
    elif commands[0] == 2:
        relement = stack.pop()
        if len(maximum) and relement == maximum[-1]:
            maximum.pop()
            if len(maximum):
                maximum_element = maximum[-1]
    else:
        print(maximum_element)



