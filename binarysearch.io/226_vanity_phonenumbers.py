class Solution:
    def solve(self, digits):
        map = {
            '2':'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        output = []
        def helper(combination, digit):
            if not len(digit):
                output.append(combination)
                return
            d = digit[0]
            for letter in map[d]:
                helper(combination + letter, digit[1:])
        helper("", digits)
        return output
            
            
            
            
        