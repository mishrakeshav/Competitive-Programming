class Solution:
    def solve(self, older, newer):
        # Write your code here
        older = list(map(int, older.split(".")))
        newer = list(map(int, newer.split(".")))
        return newer > older
    