class Solution:
    def concatenatedBinary(self, n: int) -> int:
        binary = ""

        for i in range(1, n+1):
            binary += bin(i)[2:]

        decimal = int(binary, 2)

        return decimal % (10**9 + 7)