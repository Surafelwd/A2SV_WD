class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        def turn(l,r):
            if  r == l:
                return nums[l]
            left = nums[l] - turn(l+1,r)
            right = nums[r] - turn(l, r-1)
            return max(left , right)
        return turn(0 ,n-1) >=0