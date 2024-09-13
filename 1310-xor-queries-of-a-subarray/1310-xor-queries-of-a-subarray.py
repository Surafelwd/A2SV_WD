class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(queries)
        m = len(arr)
        ans = [0] *m
        res =[]
        ans[0]=arr[0]
        for i in range(1,m):
            a= ans[i-1]^arr[i]
            ans[i] = a
        for i , j in queries:
            if i == 0:
                res.append(ans[j])
            else:
                res.append(ans[j]^ans[i-1])
        return res