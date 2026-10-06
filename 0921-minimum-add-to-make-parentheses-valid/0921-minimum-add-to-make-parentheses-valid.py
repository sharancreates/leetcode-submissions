class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        unmatched_open = 0
        moves_needed = 0
        
        for char in s:
            if char == '(':
                unmatched_open += 1
            else:  
                if unmatched_open > 0:
                    unmatched_open -= 1
                else:
                    moves_needed += 1
                    
        return moves_needed + unmatched_open
