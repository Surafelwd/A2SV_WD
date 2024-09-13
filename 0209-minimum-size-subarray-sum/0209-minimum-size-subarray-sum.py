class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        a = 0
        t =0
        c = 100000
        if sum(nums) == target:
            return len(nums)
        if sum(nums)<target:
            return 0
        for b in range(len(nums)):
            t +=nums[b]
            while  t >= target:
                c= min(c, b-a+1)
                t-=nums[a]
                a+=1
        return c