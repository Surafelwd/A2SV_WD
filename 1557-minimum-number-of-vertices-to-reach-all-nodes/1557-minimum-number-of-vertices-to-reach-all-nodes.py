class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        l = len(edges)
        holder = [0]*n
        ans = []
        for i in range(l):
            holder[edges[i][1]] =+1
        for i in range(n):
            if holder[i] == 0:
                ans.append(i)
        return ans