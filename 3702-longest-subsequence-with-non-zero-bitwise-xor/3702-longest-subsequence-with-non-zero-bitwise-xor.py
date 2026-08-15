class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)

        if all(x == 0 for x in nums):
            return 0

        xor = 0
        for x in nums:
            xor ^= x

        if xor != 0:
            return n

        return n - 1