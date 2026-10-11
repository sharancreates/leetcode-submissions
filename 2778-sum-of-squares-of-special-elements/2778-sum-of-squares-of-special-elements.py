class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        s = 0

        for idx, val in enumerate(nums):
            i = idx + 1

            if n % i == 0:
                s += val**2

        return s