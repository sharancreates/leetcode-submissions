import math

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd, even = 0, 0

        for i in range(2*n+1):
            if i % 2 == 0:
                odd += i
            else:
                even += i
        
        return math.gcd(odd, even)