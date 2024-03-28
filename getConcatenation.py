class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        num1=nums
        num1.extend(nums)
        return num1
