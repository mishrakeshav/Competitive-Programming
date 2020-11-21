class Solution:
    def solve(self, lists):
        # Write your code here
        new_list = []
        def merge(l1,l2,new_list):
            n = len(l1)
            m = len(l2)
            i = 0
            j = 0
            
            while i < n and j < m:
                if l1[i] < l2[j] :
                    new_list.append(l1[i])
                    i += 1
                else:
                    new_list.append(l2[j])
                    j += 1 
            if i < n:
                while i < n:
                    new_list.append(l1[i])
                    i += 1
            
            if j < m:
                while j < m:
                    new_list.append(l2[j])
                    j += 1
            
            return new_list
        if len(lists) == 1:
            return lists[0]
        new_list = merge(lists[0],lists[1],[])
        for i in range(2,len(lists)):
            new_list = merge(lists[i],new_list,[])
        
        return new_list
class Solution:
    def solve(self, lists):
        # Write your code here
        
        new_list = []
        for l in lists:
            new_list.extend(l)
            
        new_list.sort()
        
        return new_list