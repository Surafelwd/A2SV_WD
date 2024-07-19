class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        s = sorted(list(zip(position , speed)), reverse=True)
        n = len(s )
        c =0
        pr=0
        for i in range(n):
            t = (target - s[i][0])/s[i][1]
            if pr >= t:
                continue
            else:
                c+=1
                pr=t
        return c