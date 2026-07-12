class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(arr)
        rank = {}
        r = 1

        for num in sorted_arr:
            if num not in rank:
                rank[num] = r
                r += 1

        return [rank[num] for num in arr]