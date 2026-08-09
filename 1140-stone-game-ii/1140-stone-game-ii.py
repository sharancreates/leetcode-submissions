class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + piles[i]

        memo = {}

        def maximum(M):
            return range(1, 2 * M + 1)

        def check(i, M):
            if (i, M) in memo:
                return memo[(i, M)]
            if i + 2 * M >= n:
                return prefix[n] - prefix[i]

            best = 0

            for X in maximum(M):
                if i + X > n:
                    break

                taken = prefix[i + X] - prefix[i]

                remaining = prefix[n] - prefix[i + X]

                opponent = check(i + X, max(M, X))

                current = taken + (remaining - opponent)

                best = max(best, current)

            memo[(i, M)] = best
            return best

        return check(0, 1)