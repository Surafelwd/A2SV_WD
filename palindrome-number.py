class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=0
        z=x
        while x>0:
            y=(y*10)+ (x%10)
            x=x//10
        if y==z:
            return True
        else:
            return False
