class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        
        total_elements = n + k - 1
        to_choose = 2 * k
        
        if total_elements < to_choose:
            return 0
        num = 1
        den = 1
        for i in range(1, to_choose + 1):
            num = (num * (total_elements - i + 1)) % MOD
            den = (den * i) % MOD
            
        return (num * pow(den, MOD - 2, MOD)) % MOD