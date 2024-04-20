class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))

        def compare(a, b):
            return int(b + a) - int(a + b)

        n = len(nums)
        for i in range(n):
            for j in range(n - i - 1):
                if compare(nums[j], nums[j + 1]) > 0:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        result = ''.join(nums)

        
        result = result.lstrip('0')

        return result if result else '0'
