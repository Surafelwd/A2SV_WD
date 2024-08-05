class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        c =0
        for i in arr:
            w = arr.count(i)
            if w == 1:
                c+=1
            if c == k:
                return i
        return ''
