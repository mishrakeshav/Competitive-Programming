open_parenthesis = {
        "":"",
        '0' : "",
        '1' : "(",
        '2' : "((",
        '3' : "(((",
        '4' : "((((",
        '5' : "(((((",
        '6' : "((((((",
        '7' : "(((((((",
        '8' : "((((((((",
        '9' : "((((((((("
    }
closed_parenthesis = {
        "":"",
        '0' : "",
        '1' : ")",
        '2' : "))",
        '3' : ")))",
        '4' : "))))",
        '5' : ")))))",
        '6' : "))))))",
        '7' : ")))))))",
        '8' : "))))))))",
        '9' : ")))))))))"
    }
for t in range(int(input())):
    S = input() 
    new_s = ""  
    level = 0 
    for i in range(len(S)):
        if int(S[i]) > level:
            diff = int(S[i]) - level
            level += diff
            new_s += open_parenthesis[str(diff)] 
            new_s += S[i]
        elif int(S[i]) < level:
            diff = level - int(S[i])
            level -= diff
            new_s += closed_parenthesis[str(diff)] 
            new_s += S[i]
        else:
            new_s += S[i]
    if new_s[-1] != ")":
        new_s += closed_parenthesis[new_s[-1]]
    print("Case #{}: {}".format(t+1,new_s))

         
