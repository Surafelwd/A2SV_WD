class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        short_s=min(strs , key=len)
        for i , char in enumerate(short_s):
            for other_s in strs:
                if char!=other_s[i]:
                    return short_s[:i]
        return short_s
