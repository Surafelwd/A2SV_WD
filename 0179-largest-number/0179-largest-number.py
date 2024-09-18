class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        ar = list(map(str,nums))
        ar.sort(key = lambda x :x*10 , reverse =True)
        if ar[0] ==  "0":
            return "0"
        ans =''.join(ar)
        return ans
