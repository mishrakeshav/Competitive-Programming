from sys import stdin,stdout 
T,s = map(int, stdin.readline().split())
for t in range(int(T)):
    N = int(stdin.readline())
    a = sorted(list(map(int, stdin.readline().split())))
    b = sorted(list(map(int, stdin.readline().split())))
    table = dict() 
    flag = 0 
    if a[-1] >= b[-1]:
        stdout.write("NO" + "\n")
    else:
        if a[0] < b[0]:
            flag += 1 
            table[a[0]] = 1 
            table[b[0]] = 1 
            for i in range(1,N):
                if a[i] < b[i] and a[i] in table:
                    flag += 1 
                    table[a[i]] = 1 
                    table[b[i]] = 1 
                else:
                    break 
            if len(a)!=flag:
                # stdout.write(str(table) + "\n")
                stdout.write("NO" + "\n")
            else:
                # stdout.write(str(table) + "\n")
                stdout.write("YES"+ "\n")
        else:
            # stdout.write(str(table) + "\n")
            stdout.write("NO\n")
            
    
