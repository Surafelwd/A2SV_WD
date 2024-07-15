class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for e in logs:
            if e == '../' and stack:
                stack.pop()
            elif e == './':
                continue
            else:
                stack.append(e)
        ans = len(stack)
        return ans
