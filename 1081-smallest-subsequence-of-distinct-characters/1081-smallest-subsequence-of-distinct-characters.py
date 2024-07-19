class Solution:
    def smallestSubsequence(self, s: str) -> str:
        s1 = set()
        stack = []
        lastocc={e:i for i ,e in enumerate(s) }
        for i ,e in enumerate(s):
            if e not in s1:
                while stack and e < stack[-1] and i < lastocc[stack[-1]]:
                    s1.discard(stack.pop())
                s1.add(e)
                stack.append(e)
        return ''.join(stack)
        