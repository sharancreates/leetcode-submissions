class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()

        option1 = nums[-1] - nums[2]
        option2 = nums[-3] - nums[0]
        option3 = nums[-2] - nums[1]
        return min(option1, option2, option3)