class Solution:
    def longestPalindrome(self, s: str) -> str:
        n= len(s)
        le = 1
        sl = s[0]
        for i in range(n-1):
            for j in range(i+1, n):
                if j-i+1 > le and s[i:j+1] == s[i:j+1][::-1]:
                    le = j-i+1
                    sl = s[i:j+1]
        return sl