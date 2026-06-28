class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        n = len(arr)

        arr.sort()

        if arr[0] != 1:
            arr[0] = 1

        for i in range(n - 1):
            r = arr[i + 1] - arr[i]

            if r > 1:
                arr[i + 1] = arr[i] + 1

        return max(arr)