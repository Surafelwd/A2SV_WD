class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses={}
        for winner , loss in matches:
            losses[winner]=losses.get(winner, 0)
            losses[loss]= losses.get(loss,0) +1
        never_l= []
        los = []
        for player,losss in losses.items():
            if losss == 0:
                never_l.append(player)
            if losss ==1:
                los.append(player)
        return [sorted(never_l),sorted(los)]


        
