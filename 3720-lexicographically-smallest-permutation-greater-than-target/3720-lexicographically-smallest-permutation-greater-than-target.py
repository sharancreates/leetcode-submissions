class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = Counter(s)
        n = len(s)

        prefix_len = 0

        for i in range(n):
            if cnt[target[i]] == 0:
                break

            cnt[target[i]] -= 1
            prefix_len += 1
        for i in range(prefix_len, -1, -1):

            if i < prefix_len:
                cnt[target[i]] += 1

            if i == n:
                continue

            for c in range(ord(target[i]) + 1, ord('z') + 1):
                ch = chr(c)

                if cnt[ch] > 0:
                    cnt[ch] -= 1

                    result = target[:i] + ch

                    for x in range(26):
                        letter = chr(ord('a') + x)
                        result += letter * cnt[letter]

                    return result

        return ""
