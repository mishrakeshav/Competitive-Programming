

def solve(code):
    if len(code) <= 2:
        return len(code)
    else:
        n = len(code)
        ans = 0
        for i in range(n-2):
            if int(code[i:i+2]) <= 26:
                ans += 3 
            




if __name__ == '__main__':
    mem = {}
    while True:
        code = input()
        if code == '0':
            break
        solve(code)