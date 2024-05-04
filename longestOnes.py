class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        j=0
        zero=0
        L=0
        for i in range(len(nums)):
            if nums[i]==0:
                zero+=1
            if zero >k:
                if nums[j]==0:
                    zero-=1
                j+=1
            n=i-j+1
            L=max(L,n)
        return L

        
