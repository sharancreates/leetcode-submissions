class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = Counter(s)

        odd = [c for c in cnt if cnt[c] & 1]
        if len(odd) > 1:
            return ""

        half_cnt = [cnt[chr(ord('a') + i)] // 2 for i in range(26)]
        m = n // 2

        def build(half):
            left = ''.join(half)
            if n & 1:
                return left + odd[0] + left[::-1]
            return left + left[::-1]
        ans = []
        def dfs(pos, cmp):
            if pos == m:
                if cmp == 1:
                    return True

                candidate = build(ans)
                if candidate > target:
                    return True

                return False

            start = 0

            if cmp == 0:
                start = ord(target[pos]) - ord('a')

            for x in range(start, 26):
                if half_cnt[x] == 0:
                    continue

                ch = chr(ord('a') + x)

                new_cmp = cmp
                if cmp == 0:
                    if ch < target[pos]:
                        continue
                    elif ch > target[pos]:
                        new_cmp = 1

                half_cnt[x] -= 1
                ans.append(ch)

                if dfs(pos + 1, new_cmp):
                    return True

                ans.pop()
                half_cnt[x] += 1

            return False

        if dfs(0, 0):
            return build(ans)

        return ""
