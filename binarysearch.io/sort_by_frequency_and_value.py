from collections import Counter
class Solution:
    def solve(self, arr):
        # Write your code here
        
        c = Counter(arr)
        grp = {}
        for i in c:
            if c[i] not in grp:
                grp[c[i]] = []
            grp[c[i]].append(i)
            
        new_arr = []
        for i in sorted(grp.keys(), reverse = True):
            new_arr.extend(sorted(grp[i], reverse = True))
            
        ans = []
        for i in new_arr:
            ans.extend([i for j in range(c[i])])
            
        return ans