class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # Step 1: Factorize t into prime factors 2, 3, 5, 7
        factors = {2: 0, 3: 0, 5: 0, 7: 0}
        for p in [2, 3, 5, 7]:
            while t % p == 0:
                factors[p] += 1
                t //= p
        if t > 1:
            return "-1"
            
        n = len(num)
        
        # Helper function to find the minimum string of digits needed 
        # to satisfy the remaining prime factor requirements
        def get_min_suffix(rem_factors: dict) -> str:
            c2, c3, c5, c7 = rem_factors[2], rem_factors[3], rem_factors[5], rem_factors[7]
            
            # Form 9s from 3s
            n9 = c3 // 2
            c3 %= 2
            
            # Form 8s from 2s
            n8 = c2 // 3
            c2 %= 3
            
            # Combine remaining 2s and 3s into 6
            n6 = 0
            if c2 > 0 and c3 > 0:
                n6 = 1
                c2 -= 1
                c3 -= 1
                
            # Form 4s from remaining 2s
            n4 = c2 // 2
            c2 %= 2
            
            # Remaining counts
            n2 = c2
            n3 = c3
            n5 = c5
            n7 = c7
            
            # Assemble the digits in ascending order to make the smallest number
            return "2" * n2 + "3" * n3 + "4" * n4 + "5" * n5 + "6" * n6 + "7" * n7 + "8" * n8 + "9" * n9

        # Step 2: Check if the number itself is valid (if it is zero-free)
        if '0' not in num:
            curr_factors = {2: 0, 3: 0, 5: 0, 7: 0}
            for d in num:
                val = int(d)
                for p in [2, 3, 5, 7]:
                    while val % p == 0:
                        curr_factors[p] += 1
                        val //= p
            if all(curr_factors[p] >= factors[p] for p in [2, 3, 5, 7]):
                return num

        # Step 3: Prefix matching and Backtracking
        # Prefix factors tracking
        pref_factors = [{2: 0, 3: 0, 5: 0, 7: 0}]
        for d in num:
            val = int(d)
            next_f = pref_factors[-1].copy()
            if val > 0:
                for p in [2, 3, 5, 7]:
                    while val % p == 0:
                        next_f[p] += 1
                        val //= p
            pref_factors.append(next_f)

        # Iterate from right to left to find where we can increment a digit
        for i in range(n - 1, -1, -1):
            # If there's a 0 before or at this position in the prefix, we can't match it
            if '0' in num[:i]:
                continue
                
            curr_d = int(num[i])
            # Try to increment the digit at position i
            for d in range(curr_d + 1, 10):
                # Calculate required remaining factors
                rem_factors = {}
                val = d
                d_factors = {2: 0, 3: 0, 5: 0, 7: 0}
                for p in [2, 3, 5, 7]:
                    while val % p == 0:
                        d_factors[p] += 1
                        val //= p
                
                possible = True
                for p in [2, 3, 5, 7]:
                    needed = factors[p] - pref_factors[i][p] - d_factors[p]
                    rem_factors[p] = max(0, needed)
                
                # Get the minimum suffix sequence for these factors
                suffix = get_min_suffix(rem_factors)
                rem_len = n - 1 - i
                
                if len(suffix) <= rem_len:
                    # Pad with '1's on the left of the suffix to maintain the length
                    full_suffix = "1" * (rem_len - len(suffix)) + suffix
                    return num[:i] + str(d) + full_suffix

        # Step 4: If no number of length `n` works, find the absolute smallest larger length
        rem_factors = factors.copy()
        suffix = get_min_suffix(rem_factors)
        target_len = max(n + 1, len(suffix))
        
        return "1" * (target_len - len(suffix)) + suffix
