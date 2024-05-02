class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        trainers.sort()
        players.sort()
        player=0
        trainer=0
        count=0
        while player < len(players) and trainer < len(trainers):
            if players[player] <= trainers[trainer]:
                count+=1
                player+=1
                trainer+=1
            else:
                trainer+=1
        return count
