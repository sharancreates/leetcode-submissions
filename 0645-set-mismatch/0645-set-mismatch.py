class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set()
        number = 0
        dup = 0
        for num in nums:
            if num in seen:
                dup = num
            seen.add(num)

        for i in range(1, len(nums) + 1):
            if i not in nums:
                number = i
                break

        output = [dup, number]

        return output