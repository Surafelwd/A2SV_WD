class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        windowS= sum(nums[:k])
        avg=windowS/k
        
        for g in range(k , len(nums)):
            windowS+=nums[g]
            windowS-=nums[g-k]
            avg=max(avg , windowS/k)
        return avg
        
