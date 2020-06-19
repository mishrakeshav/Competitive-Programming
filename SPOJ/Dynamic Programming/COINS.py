
def solve(n, mem):
    if n in mem:
        return mem[n]
    else:
        mem[n] = max(
            n,
            solve(n//2,mem) + solve(n//3,mem) + solve(n//4, mem)
        )
        return mem[n]
   
    



if __name__ == '__main__':
    try:
        while True:
            n = int(input())
            mem = {}
            mem[0] = 0 
            mem[1] = 1 
            print(solve(n, mem))
    except:
        pass