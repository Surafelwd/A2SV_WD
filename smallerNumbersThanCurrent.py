class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n= len(nums)
        maxn= max(nums)
        t=maxn+1
        count=[0]*t
        for num in nums:
            count[num]+=1
        for i in range(1,t):
            count[i]+=count[i-1]
        
        sortedn=[0]*n
        for num in nums:
            sortedn[count[num]-1]=num
            count[num]-=1
        maps={}
        result=[]
        
        for  i in range(n):
            if sortedn[i] not in maps:
                maps[sortedn[i]] = i
        for i in range (n):
            result.append(maps[nums[i]])
        return result
