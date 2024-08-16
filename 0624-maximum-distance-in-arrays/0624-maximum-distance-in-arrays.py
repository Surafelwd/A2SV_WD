class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        l = arrays[0][-1]
        r = arrays[0][0]
        n = len(arrays)
        ans = 0
        for i in range(1,n):
            ans = max(abs(l - arrays[i][0]) , abs(arrays[i][-1] - r ))
            l = max(l ,arrays[i][-1] )
            r = min(r, arrays[i][0])
        
        return ans

