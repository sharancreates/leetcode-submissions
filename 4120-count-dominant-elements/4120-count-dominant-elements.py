class Solution:
    def countDominantElements(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 1

        dominant = 0
        n = len(nums)

        for i in range(n):
            if i == 0:
                if nums[0] >= nums[1]:
                    dominant += 1
            elif i == n-1:
                if nums[-1] >= nums[-2]:
                    dominant += 1
            else:
                avg = (nums[i-1]+nums[i+1])/2
                if nums[i] >= avg:
                    dominant += 1

        return dominant