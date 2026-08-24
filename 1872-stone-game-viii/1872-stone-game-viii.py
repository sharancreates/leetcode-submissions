class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        prefix = [0 for i in range(n)]

        prefix[0] = stones[0]

        for i in range(n):
            prefix[i] = prefix[i-1] + stones[i]

        best = prefix[n-1]
        for i in range(n-2, 0, -1):
            best= max(best, prefix[i] -best)

        return best