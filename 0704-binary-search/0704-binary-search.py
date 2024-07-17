class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0 
        h = n-1
        while l <= h:
            a =( l+h)//2
            if nums[a] == target:
                return a
            elif nums[a] < target :
                l = a+1
            else:
                h= a-1
        return -1

        