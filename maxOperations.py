class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        count=0
        left=0
        right=len(nums)-1
        while   left < right:
            if  nums[left] + nums[right] == k:
                right-=1
                left+=1
                count+=1
            elif nums[right] + nums[left] > k:
                right-=1
            else:
                left+=1
        return  count
                
