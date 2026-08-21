import math

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins = sorted(list(set(coins)))
        filtered_coins = []
        for c in coins:
            if not any(c % x == 0 for x in filtered_coins):
                filtered_coins.append(c)
        coins = filtered_coins
        n = len(coins)
        
        lcm_combos = []
        
        def backtrack(index, current_lcm, count):
            if index == n:
                if count > 0:
                    sign = 1 if count % 2 == 1 else -1
                    lcm_combos.append((current_lcm, sign))
                return
            
            backtrack(index + 1, current_lcm, count)
            
            next_lcm = (current_lcm * coins[index]) // math.gcd(current_lcm, coins[index])
            backtrack(index + 1, next_lcm, count + 1)
            
        backtrack(0, 1, 0)
        
        def count_multiples(m: int) -> int:
            total = 0
            for lcm_val, sign in lcm_combos:
                total += sign * (m // lcm_val)
            return total

        low = 1
        high = min(coins) * k
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            if count_multiples(mid) >= k:
                ans = mid
                high = mid - 1  
            else:
                low = mid + 1  
                
        return ans
