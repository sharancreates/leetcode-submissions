from math import comb

class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        
        def dfs(elements):
            if len(elements) <= 2:
                return 1
            
            root = elements[0]
            left = [x for x in elements if x < root]
            right = [x for x in elements if x > root]
            
            return comb(len(left) + len(right), len(left)) * dfs(left) * dfs(right) % MOD
            
        return (dfs(nums) - 1) % MOD
