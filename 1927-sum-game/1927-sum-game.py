class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        mid = n // 2
        left_half = num[:mid]
        right_half = num[mid:]

        sum_l = 0
        for char in left_half:
            if char != '?':
                sum_l += int(char)

        sum_r = 0
        for char in right_half:
            if char != '?':
                sum_r += int(char)
        
        q_l = left_half.count('?')
        q_r = right_half.count('?')
        
        if (q_l + q_r) % 2 != 0:
            return True
            
        return (sum_l - sum_r) * 2 != (q_r - q_l) * 9
