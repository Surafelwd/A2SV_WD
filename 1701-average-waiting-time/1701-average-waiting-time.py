class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n= len(customers)
        s=0
        c=0
        a = customers[0][0]+customers[0][1]
        for i in range(n):
            if a > customers[i][0] and i >0:
                a+= customers[i][1]
                s+=(a- customers[i][0])
            else:
                a = customers[i][0]+customers[i][1]
                s+=(a- customers[i][0])
        return (s/n)