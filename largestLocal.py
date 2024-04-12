class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        new=[]
        for i in range(1,len(grid)-1):
            newg=[]
            for j in range(1,len(grid)-1):
                maxV=max(
                    grid[i-1][j-1], grid[i-1][j], grid[i-1][j+1],
                    grid[i][j-1], grid[i][j], grid[i][j+1],
                    grid[i+1][j-1], grid[i+1][j], grid[i+1][j+1])
                newg.append(maxV)
            new.append(newg)
        return new
