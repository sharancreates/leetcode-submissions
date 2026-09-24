class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            sum_ = 0
            a = str(nums[i])
            for j in a:
                sum_ = sum_ + int(j)
            if sum_ == i:
                return i
        return -1