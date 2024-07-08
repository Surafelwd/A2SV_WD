class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n= len(p)
        pc = Counter(p)
        sc= Counter(s[:n-1])
        ans = []
        for i in range(n-1, len(s)):
            sc+=Counter(s[i])
            if pc == sc:
                ans.append(i-n+1)
            sc[s[i-n+1]]-=1
            if sc[s[i-n+1]] == 0:
                del sc[s[i-n+1]]
        return ans

