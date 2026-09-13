class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        points1 = [(r, c) for r, row in enumerate(img1) for c, val in enumerate(row) if val == 1]
        points2 = [(r, c) for r, row in enumerate(img2) for c, val in enumerate(row) if val == 1]
        
        translation_counts = defaultdict(int)
        max_overlap = 0
        
        for r1, c1 in points1:
            for r2, c2 in points2:
                vector = (r2 - r1, c2 - c1)
                translation_counts[vector] += 1
                max_overlap = max(max_overlap, translation_counts[vector])
                
        return max_overlap
