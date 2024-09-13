class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans =[]
        dic1 = {}
        if len(s) < 10:
            return []
        for i in range(len(s)-9):
            sq = s[i:i+10]
            if sq  in dic1:
                dic1[sq]+=1
            else:
                dic1[sq] = 1
        for sq , c in dic1.items():
            if c>1:
                ans.append(sq)
        return ans