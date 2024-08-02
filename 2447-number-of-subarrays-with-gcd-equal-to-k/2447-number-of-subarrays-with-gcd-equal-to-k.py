class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        ans = 0
        
        for i in range (len (nums)):
            c = nums [i]
            
            for j in range(i, len(nums)):
                c = math.gcd(c,nums[j])
                if k == c:
                    ans+=1
                if c < k:
                    break
        return ans
            
            