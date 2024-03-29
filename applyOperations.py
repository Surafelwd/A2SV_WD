class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i=0
        j=1
        while j < len(nums):
            if nums[i] == nums[j]:
                nums[i]*=2
                nums[j]=0
                i+=1
                j+=1
            else:
                i+=1
                j+=1
        nums=[num for num in nums if num != 0 ] + [0]*nums.count(0)
        return nums
