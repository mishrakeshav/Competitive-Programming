class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx_diff = 0
        if len(prices) == 0:
            return 0
        mi_element = prices[0]
        
        for i in range(1,len(prices)):
            if prices[i] - mi_element > mx_diff:
                mx_diff = prices[i] - mi_element 
            
            if prices[i] < mi_element:
                mi_element = prices[i]
            
        return mx_diff
        