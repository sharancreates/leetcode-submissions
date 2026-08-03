class Solution:
    def stoneGameIII(self, stoneValue):
        memo = {}

        def dfs(i):
            if i >= len(stoneValue):
                return 0

            if i in memo:
                return memo[i]

            best = float('-inf')
            total = 0

            for k in range(3):
                if i + k < len(stoneValue):
                    total += stoneValue[i + k]
                    best = max(best, total - dfs(i + k + 1))

            memo[i] = best
            return best

        diff = dfs(0)

        if diff > 0:
            return "Alice"
        elif diff < 0:
            return "Bob"
        else:
            return "Tie"