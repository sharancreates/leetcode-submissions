class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans1 = nums[:n]
        ans2 = nums[n:]
        ans = []
        for i in range(n):
            ans.append(ans1[i])
            ans.append(ans2[i])
        return ans