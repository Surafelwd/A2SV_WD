class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxs = max(nums)
        c,l =0,1
        for i in nums :
            if i == maxs:
                c+=1
                l = max(l,c)
            else:
                c=0
        return l