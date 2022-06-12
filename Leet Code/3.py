def solve(s):
    freq = dict()
    j = 0
    max_len = 0  
    for i in range(len(s)):
        if freq.get(s[i],-1) >= 0:
            j = max(freq[s[i]] + 1,j) 
        
        freq[s[i]] = i 
        max_len = max(max_len, i - j + 1)
    return max_len



for _ in range(int(input())):
    s = input()
    print(solve(s))