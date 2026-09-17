class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        min_len = [float('inf')] * n
        
        left = 0
        current_sum = 0
        min_total_length = float('inf')
        best_till_now = float('inf')
        
        for right in range(n):
            current_sum += arr[right]
            
            while current_sum > target and left <= right:
                current_sum -= arr[left]
                left += 1
                
            if current_sum == target:
                current_len = right - left + 1
                
                if left > 0 and min_len[left - 1] != float('inf'):
                    min_total_length = min(min_total_length, current_len + min_len[left - 1])
                
                best_till_now = min(best_till_now, current_len)
            
            min_len[right] = best_till_now
            
        return min_total_length if min_total_length != float('inf') else -1
