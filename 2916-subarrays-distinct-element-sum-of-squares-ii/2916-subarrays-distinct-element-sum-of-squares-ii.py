class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.sum_sq = [0] * (4 * n)
        self.sum_val = [0] * (4 * n)
        self.lazy = [0] * (4 * n)
        self.MOD = 10**9 + 7

    def _push_down(self, node, start, end):
        if self.lazy[node] == 0:
            return
        
        lazy_val = self.lazy[node]
        mid = (start + end) // 2
        left_len = mid - start + 1
        right_len = end - mid
        
        # Update left child
        left_child = 2 * node
        self.sum_sq[left_child] = (self.sum_sq[left_child] + 2 * lazy_val * self.sum_val[left_child] + lazy_val * lazy_val * left_len) % self.MOD
        self.sum_val[left_child] = (self.sum_val[left_child] + lazy_val * left_len) % self.MOD
        self.lazy[left_child] = (self.lazy[left_child] + lazy_val) % self.MOD
        
        # Update right child
        right_child = 2 * node + 1
        self.sum_sq[right_child] = (self.sum_sq[right_child] + 2 * lazy_val * self.sum_val[right_child] + lazy_val * lazy_val * right_len) % self.MOD
        self.sum_val[right_child] = (self.sum_val[right_child] + lazy_val * right_len) % self.MOD
        self.lazy[right_child] = (self.lazy[right_child] + lazy_val) % self.MOD
        
        self.lazy[node] = 0

    def update(self, node, start, end, l, r, val):
        if l <= start and end <= r:
            length = end - start + 1
            self.sum_sq[node] = (self.sum_sq[node] + 2 * val * self.sum_val[node] + val * val * length) % self.MOD
            self.sum_val[node] = (self.sum_val[node] + val * length) % self.MOD
            self.lazy[node] = (self.lazy[node] + val) % self.MOD
            return
            
        self._push_down(node, start, end)
        mid = (start + end) // 2
        
        if l <= mid:
            self.update(2 * node, start, mid, l, r, val)
        if r > mid:
            self.update(2 * node + 1, mid + 1, end, l, r, val)
            
        self.sum_sq[node] = (self.sum_sq[2 * node] + self.sum_sq[2 * node + 1]) % self.MOD
        self.sum_val[node] = (self.sum_val[2 * node] + self.sum_val[2 * node + 1]) % self.MOD


class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        tree = SegmentTree(n)
        
        last_seen = {}
        total_sum_squares = 0
        
        for j in range(n):
            # Find the last occurrence of the current number
            last_idx = last_seen.get(nums[j], -1)
            
            # Increment distinct counts for all subarrays starting from last_idx + 1 to j
            tree.update(1, 0, n - 1, last_idx + 1, j, 1)
            
            # The root node (1) contains the total sum of squares for subarrays ending at index j
            total_sum_squares = (total_sum_squares + tree.sum_sq[1]) % MOD
            
            # Update the last seen position of the element
            last_seen[nums[j]] = j
            
        return total_sum_squares
