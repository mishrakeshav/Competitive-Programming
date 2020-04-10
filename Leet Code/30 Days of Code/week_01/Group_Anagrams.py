from collections import defaultdict
def groupAnagrams(strs):
    ans = defaultdict(list)
    for s in strs:
        count = [0]*26

        for c in s:
            count[ord(c)-ord("a")] += 1 
        ans[tuple(count)].append(s)
    return ans.values()


for t in range(int(input())):
    N = int(input())
    strs = []
    for i in range(N):
        strs.append(input())
    print(groupAnagrams(strs))
