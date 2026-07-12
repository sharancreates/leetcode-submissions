class Solution:
    def reverseBits(self, n: int) -> int:
        binary_n = bin(n)[2:].zfill(32)
        rev = (binary_n)[::-1]

        ans = int((rev), 2)

        return ans