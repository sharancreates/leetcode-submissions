class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        digit_counts = Counter(digits)
        result = []
        
        for num in range(100, 1000, 2):
            d1 = num // 100
            d2 = (num // 10) % 10
            d3 = num % 10
            
            needed = Counter([d1, d2, d3])
            
            if all(digit_counts[d] >= needed[d] for d in needed):
                result.append(num)
                
        return len(result)