class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        def tp(ls , l, r):
            while l < r:
                ls[l], ls[r] = ls[r], ls[l]
                l+=1
                r-=1
        if k>n:
            k= k%n
        if k > 0:
            tp(nums, 0 , n-1)
            tp(nums,0 , k-1 )
            tp(nums,k, n-1)
        return nums
                
        