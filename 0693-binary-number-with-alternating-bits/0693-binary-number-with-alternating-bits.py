class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binary_n = bin(n)[2:]

        first = binary_n[0]

        for i in range(0, len(binary_n), 2):
            if binary_n[i] != first:
                return False

        if len(binary_n) > 1:
            second = binary_n[1]
            for i in range(1, len(binary_n), 2):
                if binary_n[i] != second:
                    return False

            if first == second:
                return False

        return True