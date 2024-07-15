class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        k =0
        for e in s:
            if e =='(':
                stack.append(0)
            else:
                k = max(1, stack.pop()*2)
                stack[-1] +=k
        return stack.pop()