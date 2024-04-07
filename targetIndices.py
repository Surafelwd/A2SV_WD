class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        output=[]
        n= len(nums)
        for i in range(n):
            for j in range(0,n-i-1):
                if nums[j] > nums[j+1]:
                     nums[j], nums[j + 1] = nums[j + 1], nums[j]
        for i,num in enumerate(nums) :
            if num==target:
                output.append(i)
        return output
