from collections import defaultdict
def solve(nums):
    i = j = 0
    max_score = 0  
    curr_summ = 0 
    freq = defaultdict(int)
    
    for i in range(len(nums)):
        while freq[nums[i]] > 0:
            curr_summ -= nums[j]
            freq[nums[j]] -= 1 
            j += 1 
        freq[nums[i]] += 1 
        curr_summ += nums[i]
        max_score = max(max_score,curr_summ)

    max_score = max(max_score,curr_summ)

    return max_score

def solve(nums):
    def get_range_sum(i,j,prefix):
        if j - 1 < 0:
            return prefix[i]
        return prefix[i] - prefix[j-1]
        
    i = j = 0 
    freq = dict()
    max_score = 0 

    prefix = [0 for i in range(len(nums))]
    prefix[0] = nums[0]
    for i in range(1,len(nums)):
        prefix[i] = prefix[i-1] + nums[i]

    for i in range(len(nums)):
        if freq.get(nums[i],-1) >= 0:
            j = max(freq[nums[i]] + 1,j) 
        freq[nums[i]] = i 
        max_score = max(max_score, get_range_sum(i,j,prefix))
    return max_score

def solve(nums):
    i = j = 0
    max_score = 0  
    curr_summ = 0 
    freq = defaultdict(int)
    
    for i in range(len(nums)):
        while freq[nums[i]] > 0:
            curr_summ -= nums[j]
            freq[nums[j]] -= 1 
            j += 1 
        freq[nums[i]] += 1 
        curr_summ += nums[i]
        max_score = max(max_score,curr_summ)

    max_score = max(max_score,curr_summ)

    return max_score

for _ in range(int(input())):
    nums = list(map(int,input().split()))
    max_score = solve(nums)
    print(max_score)
