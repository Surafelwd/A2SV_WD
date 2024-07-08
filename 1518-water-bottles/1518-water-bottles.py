class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        nb = numBottles
        ne = numExchange
        t=nb
        if nb < ne:
            return int(t)
        for i in range(nb):
            if nb%ne == 0:
                t+=nb/ne
                nb = nb/ne
            elif nb %ne !=0 and ne < nb:
                t+=nb//ne
                nb = nb//ne + nb%ne
        return int(t)
