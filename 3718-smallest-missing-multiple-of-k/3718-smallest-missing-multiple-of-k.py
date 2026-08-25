class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        a = False
        i = 1
        n = k
        while a == False:
            if n not in nums:
                return n
            i+=1
            n=k*i
        