class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i , ch in enumerate(s):
            lastIndex [ch] =i
        
        ans=[]
        end=0
        size=0
        for i , ch in enumerate(s):
            size+=1
            end=max(end , lastIndex[ch])
            if end==i:
                ans.append(size)
                size=0
        return ans
