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
        d=0
        if k == len(tickets)-1:
            return c
        else:
            for a in range (k+1 ,k+len(tickets[k:])):
                if tickets[k] <= tickets[a]:
                    d+=1
        return c-d
        
        