class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words:
            return []
        common=[]
        firstword=words[0]
        for char in firstword:
            if all(char in word for word in words[1:]):
                common.append(char)
                words=[word.replace(char, "",1) for word in words]
        return common
