class Solution:
    def countCommas(self, n: int) -> int:
        if len(str(n)) > 3:
            return n-999
        else:
            return 0