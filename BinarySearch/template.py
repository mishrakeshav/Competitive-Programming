"""
Article : https://leetcode.com/discuss/general-discussion/786126/python-powerful-ultimate-binary-search-template-solved-many-problems
we only need to modify three parts after copy-pasting this template, 
and never need to worry about corner cases and bugs in code any more:

1. Correctly initialize the boundary variables left and right to specify search space.
Only one rule: set up the boundary to include all possible elements

2. Decide return value. Is it return left or return left - 1?
Remember this: after exiting the while loop, left is the minimal k​ satisfying the condition function;

3. Design the condition function. This is the most difficult and most beautiful part. Needs lots of practice.
"""

def binary_search(array) -> int:
    def condition(value) -> int:
        pass 
    left , right = min(search_space) , max(search_space)
    while left < right:
        mid = left + (right - left)//2 
        if condition(mid):
            right = mid 
        else:
            left = mid + 1 
    return left 
