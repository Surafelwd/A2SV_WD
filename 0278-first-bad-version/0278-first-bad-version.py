# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        i = 1 
        j = n
        while j > i:
            a = (j+i)//2
            if isBadVersion(a):
                j = a
            else:
                i =a+1
        return i