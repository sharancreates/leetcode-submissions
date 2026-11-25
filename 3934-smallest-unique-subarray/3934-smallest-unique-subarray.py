from collections import Counter
from typing import List

class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        # Shift elements to ensure positive values for hashing
        OFFSET = 10**9 + 7
        arr = [x + OFFSET for x in nums]
        
        MOD1, BASE1 = 10**9 + 7, 1315423911
        MOD2, BASE2 = 10**9 + 9, 2654435761

        def has_unique(length: int) -> bool:
            h1 = h2 = 0
            p1 = pow(BASE1, length, MOD1)
            p2 = pow(BASE2, length, MOD2)
            
            # Initial window of size `length`
            for i in range(length):
                h1 = (h1 * BASE1 + arr[i]) % MOD1
                h2 = (h2 * BASE2 + arr[i]) % MOD2
                
            counts = Counter([(h1, h2)])
            
            # Slide the window across the array
            for i in range(length, n):
                h1 = (h1 * BASE1 - arr[i - length] * p1 + arr[i]) % MOD1
                h2 = (h2 * BASE2 - arr[i - length] * p2 + arr[i]) % MOD2
                counts[(h1, h2)] += 1
                
            return any(freq == 1 for freq in counts.values())

        left, right = 1, n
        ans = n
        
        while left <= right:
            mid = (left + right) // 2
            if has_unique(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return ans
