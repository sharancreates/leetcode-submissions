class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        def calculate_cost(k: int) -> int:
            rem1 = max(0, need1 - k)
            rem2 = max(0, need2 - k)
            return k * costBoth + rem1 * cost1 + rem2 * cost2

        candidate_1 = calculate_cost(0)
        candidate_2 = calculate_cost(min(need1, need2))
        candidate_3 = calculate_cost(max(need1, need2))
        
        return min(candidate_1, candidate_2, candidate_3)