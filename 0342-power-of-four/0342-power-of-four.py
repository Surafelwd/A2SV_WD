class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while True:
            w = (n/4)
            if n== 1:
                break
            elif n < 1:
                return False
            else:
                n=w
        return True