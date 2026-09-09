class Solution:
    def countCommas(self, n: int) -> int:
        total_commas = 0
        a = 1000
        while n >= a:
            total_commas += (n - a + 1)
            a *= 1000 
            
        return total_commas
