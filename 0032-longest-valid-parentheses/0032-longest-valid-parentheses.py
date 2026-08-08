class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = 0
        count = 0
        start = 0
        for i in range(len(s)):
            if s[i] == '(':
                count += 1
            else:
                count -= 1

            if count < 0:
                count = 0
                start = i + 1

            if count == 0:
                n = max(n, i - start + 1)
        count = 0
        start = len(s) - 1

        for i in range(len(s) - 1, -1, -1):
            if s[i] == ')':
                count += 1
            else:
                count -= 1

            if count < 0:
                count = 0
                start = i - 1

            if count == 0:
                n = max(n, start - i + 1)

        return n