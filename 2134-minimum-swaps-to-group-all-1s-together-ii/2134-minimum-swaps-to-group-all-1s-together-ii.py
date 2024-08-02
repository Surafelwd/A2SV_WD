class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        
        c = nums.count(1)
        if c == 0:
            return 0
        window =  nums[0:c]
        n= len(nums)
        a =[]
        for i in range(c):
            nums.append(nums[i])
        n= len(nums)
        for j in range(c,n):
           a.append(window.count(0))
           window.pop(0)
           window.append(nums[j])
        ans = min(a)
        return ans