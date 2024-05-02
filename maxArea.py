class Solution:
    def maxArea(self, height: List[int]) -> int:
        n= len(height)
        left=0
        right=n-1
        sum=0
        while left < right:
            if height[left] < height[right]:
                sum=max(sum, (right-left)*height[left])
                left+=1
            else:
                sum=max(sum, (right-left)*height[right])
        
                right-=1
        return sum
