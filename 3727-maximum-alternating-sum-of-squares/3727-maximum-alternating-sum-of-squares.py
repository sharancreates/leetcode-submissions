class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        squares = [x * x for x in nums]
        squares.sort()
        
        n = len(squares)
        num_pos = (n + 1) // 2
        pos_sum = sum(squares[-num_pos:])
        neg_sum = sum(squares[:-num_pos])
        
        return pos_sum - neg_sum