class Solution:
    def interpret(self, command: str) -> str:
        i=0
        result=""
        while i<len(command):
            if command[i]=="(" and command[i+1]==")":
                result+="o"
                i+=2
            elif command[i]=="(" and command[i+1]== "a" and command[i+2]=="l" and command[i+3]==")":
                result+="al"
                i+=3
            elif command[i]=="G":
                result+="G"
                i+=1
            else:
                i+=1
        return result
