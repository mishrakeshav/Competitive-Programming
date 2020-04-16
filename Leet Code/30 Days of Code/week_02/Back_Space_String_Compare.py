import itertools
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        def compare(string):
            skip = 0
            for x in reversed(string):
                if x == "#":
                    skip += 1
                elif skip:
                    skip -=1
                else:
                    yield x
        
        return all(x==y for x,y in itertools.izip_longest(compare(S),compare(T)))

c = Solution()
print(c.backspaceCompare("a#c","b"))