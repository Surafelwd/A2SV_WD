class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        n = len(word1)
        m = len(word2)
        merge = ""

        while i < n and j < m:
            if word1[i] > word2[j]:
                merge += word1[i]
                i += 1
                
            elif word1[i] < word2[j]:
                merge += word2[j]
                j += 1
                
            else:
                if word1[i:] >= word2[j:]:
                    merge += word1[i]
                    i += 1
                    
                else:
                    merge += word2[j]
                    j += 1
                    
        
        merge += word1[i:] + word2[j:]
        return merge
