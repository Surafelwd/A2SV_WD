class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        c=0
        queue = []
        for i in range(len(tickets)+1):
            if queue and queue[0] < tickets[k]:
                c+=queue[0]
                queue.pop(0)
            elif queue:
                c+=(tickets[k])
                queue.pop(0)
            if i < (len(tickets)):
                queue.append(tickets[i])
        return c
        
        