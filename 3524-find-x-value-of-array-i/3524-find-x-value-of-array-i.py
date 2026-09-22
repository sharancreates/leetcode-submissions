class Solution:
    def resultArray(self, nums: list[int], k: int) -> list[int]:
        result = [0] * k
        
        dp = [0] * k
        
        for num in nums:
            new_dp = [0] * k
            num_mod = num % k
            
            new_dp[num_mod] += 1
            
            for prev_rem in range(k):
                if dp[prev_rem] > 0:
                    new_rem = (prev_rem * num_mod) % k
                    new_dp[new_rem] += dp[prev_rem]
            
            for rem in range(k):
                result[rem] += new_dp[rem]
                
            dp = new_dp
            
        return result
