class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = []
        for i in nums:
            digits = [int(x) for x in str(i)]
            result.append(digits)

        return [x for row in result for x in row]