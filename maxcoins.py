class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        n= len(piles)//3
        j=0
        total=0
        for _ in range (n):
            total+=piles[j+1]
            j+=2
        return total


        
