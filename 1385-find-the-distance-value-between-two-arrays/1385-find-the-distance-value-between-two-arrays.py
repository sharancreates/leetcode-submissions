class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        ans = 0
        flag = 0
        for i in range(len(arr1)):
            val = arr1[i]
            flag = 0
            for j in range(len(arr2)):
                if (abs(val - arr2[j]) <= d):
                    flag = 1
                    break
            if flag == 0:
                ans += 1

        return ans