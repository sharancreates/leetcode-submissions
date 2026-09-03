class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            n = nums[i]
            a = 0
            for j in nums:
                if j < n:
                    a += 1
            ans.append(a)

        return ans