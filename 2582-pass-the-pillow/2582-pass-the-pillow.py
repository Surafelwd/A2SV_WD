class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        d= True
        i=1
        while i < n+1 and time >0:
            if i <= n and d:
                if i == n:
                    #time-=1
                    d= False
                else:
                    i+=1
                    time-=1
            else:
                i-=1
                time-=1
            if i == 1:

                d= True
        return i

