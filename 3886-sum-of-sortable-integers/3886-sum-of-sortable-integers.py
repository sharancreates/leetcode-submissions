class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        sorted_nums = sorted(nums)
        
        def is_subarray(A: list[int], B: list[int]) -> bool:
            m, l = len(A), len(B)
            if m > l: return False
            if m == 0: return True
            
            # Compute KMP pi array
            pi = [0] * m
            for i in range(1, m):
                j = pi[i - 1]
                while j > 0 and A[i] != A[j]:
                    j = pi[j - 1]
                if A[i] == A[j]:
                    j += 1
                pi[i] = j
            
            # Match A within B
            j = 0
            for i in range(l):
                while j > 0 and B[i] != A[j]:
                    j = pi[j - 1]
                if B[i] == A[j]:
                    j += 1
                if j == m:
                    return True
            return False

        def is_cyclic_shift(A: list[int], B: list[int]) -> bool:
            # A must be a contiguous subarray of B + B
            return is_subarray(A, B + B)

        total_sum = 0
        
        # Test every divisor k of n
        for k in range(1, n + 1):
            if n % k != 0:
                continue
                
            possible = True
            for i in range(0, n, k):
                A = nums[i : i + k]
                B = sorted_nums[i : i + k]
                
                if not is_cyclic_shift(A, B):
                    possible = False
                    break
                    
            if possible:
                total_sum += k
                
        return total_sum
