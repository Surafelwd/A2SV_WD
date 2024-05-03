class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = "" 
        i, j = 0, 0
        for i in range(len(s)):
            if j < len(spaces) and i == spaces[j]:
                result += " " + s[i]
                j += 1
            else:
                result += s[i]
        return result
