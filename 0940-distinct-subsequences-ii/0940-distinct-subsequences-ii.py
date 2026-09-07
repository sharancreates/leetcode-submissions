class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        total_subsequences = 0
        
        last_added = {}
        
        for char in s:
            new_combinations = (total_subsequences + 1) % MOD
            net_new = (new_combinations - last_added.get(char, 0)) % MOD
            total_subsequences = (total_subsequences + net_new) % MOD
            last_added[char] = new_combinations
            
        return total_subsequences
