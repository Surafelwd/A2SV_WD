class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 3:
            return False
        if n%3 == 0:
            if n ==3:
                return True
        else:
            return False
        return self.isPowerOfThree(n/3)