class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = []
        n = rowIndex
        for i in range(n+1):
            l =  math.factorial(n) // (math.factorial(i) * math.factorial(n - i))
            ans.append(l)
        return ans