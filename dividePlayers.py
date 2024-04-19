class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left=0
        right=len(skill)-1
        sums=0
        if len(skill)==2:
            return skill[0]*skill[1]
        while right > left :
            if skill[left] + skill[right] == skill[left+1] + skill[right-1]:
                sums += skill[right]*skill[left]
                left+=1
                right-=1
                
            else:
                return -1
        return sums
        
