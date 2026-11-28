from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        max_factor = max(factor for factor, _ in items)
        
        # 1. Count frequency of each factor
        freq = [0] * (max_factor + 1)
        for factor, _ in items:
            freq[factor] += 1
            
        # 2. Sieve-like sum to find how many items have a factor divisible by f
        divisible_count = [0] * (max_factor + 1)
        for f in range(1, max_factor + 1):
            if freq[f] > 0:
                for multiple in range(f, max_factor + 1, f):
                    divisible_count[f] += freq[multiple]
                    
        # 3. Sort items by price ascending
        items.sort(key=lambda x: x[1])
        min_price = items[0][1]
        
        total_items = 0
        rem_budget = budget
        
        # 4. Greedily buy "2-for-1" copies while price < 2 * min_price
        for factor, price in items:
            if price >= 2 * min_price or rem_budget < price:
                break
            
            # Exclude item i itself from its free copy candidates
            gain = divisible_count[factor] - 1
            if gain <= 0:
                continue
                
            can_buy = min(gain, rem_budget // price)
            total_items += can_buy * 2
            rem_budget -= can_buy * price
            
        # 5. Spend any leftover budget on the cheapest item
        total_items += rem_budget // min_price
        
        return total_items
