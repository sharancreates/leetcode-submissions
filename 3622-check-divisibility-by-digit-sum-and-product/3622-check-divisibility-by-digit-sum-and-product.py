class Solution:
    def checkDivisibility(self, n: int) -> bool:
        summ = 0
        product = 1

        for digit in str(n):
            digit = int(digit)
            summ += digit
            product *= digit

        s = summ + product

        return n % s == 0