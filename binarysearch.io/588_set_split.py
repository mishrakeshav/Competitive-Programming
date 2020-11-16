class Solution:
    def solve(self, nums):
        nums.sort()
        ls  = 0
        rs = 0 
        lset = dict()
        rset = dict()
        flag = False 
        for i in nums:
            if i not in rset:
                rset[i] = 0
            rset[i] += 1
            rs += i 
        for i in nums:
            if ls == rs:
                flag = True 
                break 
            if i not in lset:
                lset[i] = 0 
            lset[i] += 1 
            if i in rset:
                rset[i] -= 1 
            ls += i
            rs -= i 
        for i in lset:
            if i in rset and rset[i] >= 1:
                return False 
        return flag 