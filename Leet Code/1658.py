def solution(nums,x,i,j,ans):
    if i > j:
        return float('inf')   
    if x - nums[i] == 0 or x - nums[j] == 0:
        return ans + 1  
    final_ans = float('inf')
    if x - nums[i] > 0:
        final_ans = min(solution(nums,x - nums[i], i + 1, j, ans + 1),final_ans)
    if x - nums[j] > 0:
        final_ans = min(solution(nums,x - nums[j], i, j - 1, ans + 1),final_ans)
    
    return final_ans

def get_range_sum(sidx,eidx,prefix,suffix,total):
    if sidx == 0 and eidx + 1 == len(prefix):
        return total
    if sidx == 0:
        return total - suffix[eidx + 1] 
    if eidx + 1 == len(prefix):
        return total - prefix[sidx - 1]
    return total - prefix[sidx - 1] - suffix[eidx + 1]



def solution(nums,x):
    n = len(nums)
    if sum(nums) == x:
        return len(nums)
    prefix = [0 for i in range(n)]
    suffix = [0 for i in range(n)]
    prefix[0] = nums[0]
    for i in range(1,n):
        prefix[i] = prefix[i-1] + nums[i]
    suffix[-1] = nums[-1]
    for i in range(n-2,-1,-1):
        suffix[i] = suffix[i + 1] + nums[i]
    
    steps = float('inf')
    for i in range(n):
        left,right = i, n-1 
        while left < right:
            mid = (left + right)//2 
            if get_range_sum(i,mid,prefix,suffix,x) >= 0:
                right = mid 
            else:
                left = mid + 1 
        # print(i,left,get_range_sum(i,left,prefix,suffix,x))
        if get_range_sum(i,left,prefix,suffix,x) == 0:
            steps = min(i + n - left - 1, steps)
    return steps 


def solution(nums,x):
    target = sum(nums) - x 
    sidx = curr = 0
    ans = -1 
    for eidx in range(len(nums)):
        curr += nums[eidx]
        while sidx <= eidx and curr > target:
            curr -= nums[sidx]
            sidx += 1 
        if curr == target:
            ans = max(ans,eidx- sidx + 1)

    return len(nums) - ans if ans != -1 else ans  



for _ in range(int(input())):
    arr = list(map(int,input().split()))
    x = int(input())
    result = solution(arr,x)
    if result == float('inf'):
        print(-1)
    else:
        print(result)

        
