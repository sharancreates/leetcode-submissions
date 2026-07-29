class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = [0] * 26
        for c in s:
            freq[ord(c) - 97] += 1

        half = [x // 2 for x in freq]
        mid = ""

        for i, x in enumerate(freq):
            if x % 2:
                mid = chr(i + 97)

        def countWays(cnt):
            total = sum(cnt)

            # multinomial = total! / product(cnt!)
            # calculate using combinations:
            ans = 1
            left = total

            for x in cnt:
                if x == 0:
                    continue

                # choose positions for this character
                for t in range(1, x + 1):
                    ans = ans * (left - x + t) // t
                    if ans >= k:
                        return k
                left -= x

            return ans

        if countWays(half) < k:
            return ""

        res = []

        for _ in range(sum(half)):
            for i in range(26):
                if half[i] == 0:
                    continue

                half[i] -= 1
                ways = countWays(half)

                if ways >= k:
                    res.append(chr(i + 97))
                    break
                else:
                    k -= ways
                    half[i] += 1

        left = "".join(res)
        return left + mid + left[::-1]