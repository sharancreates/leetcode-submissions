class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        import collections

        row_map = collections.defaultdict(int)
        for row, seat in reservedSeats:
            row_map[row] |= 1 << seat

        res = n * 2

        for row, mask in row_map.items():
            left_free = (mask & (1 << 2 | 1 << 3 | 1 << 4 | 1 << 5)) == 0
            right_free = (mask & (1 << 6 | 1 << 7 | 1 << 8 | 1 << 9)) == 0
            mid_free = (mask & (1 << 4 | 1 << 5 | 1 << 6 | 1 << 7)) == 0

            if left_free and right_free:
                continue  
            elif left_free or right_free or mid_free:
                res -= 1  
            else:
                res -= 2  
        return res
