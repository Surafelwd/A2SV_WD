class Solution:
    def countSeniors(self, details: List[str]) -> int:
        f=11
        s=12
        a=0
        for i in details:
            age = i[f]+i[s]
            if age > '60':
                a+=1
        return a
