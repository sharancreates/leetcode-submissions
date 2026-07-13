class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = "123456789"
        ans = []

        low_len = len(str(low))
        high_len = len(str(high))

        for l in range(low_len, high_len + 1):
            for s in range(10 - l):
                num = int(digits[s:s + l])
                if low <= num <= high:
                    ans.append(num)

        return ans