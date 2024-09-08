class Solution:
    def findLHS(self, nums: List[int]) -> int:
        set1 = (nums)
        dic1 ={}
        for i in nums:
            if i in dic1:
                dic1[i]+=1
            else:
                dic1[i] =1
        n = max(nums)
        ans =0
        for i in dic1:
            if i+1 in dic1:
                sums = dic1[i+1]+dic1[i]
                ans = max(ans , sums)
        return ans

