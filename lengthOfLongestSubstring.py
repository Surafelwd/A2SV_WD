class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        j=0
        seen=set()
        maxl=0
        while i<len(s):
            if s[i] not in seen:
                seen.add(s[i])
                length=i-j+1
                maxl=max(maxl,length)
                i+=1
            else:
                seen.remove(s[j])
                j+=1
        return maxl


        
