class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = [(0,0,0)]
        ans=0
        for i in range(len(arr)):
            c=1
            while stack[-1][0] > arr[i]:
                c+=stack[-1][1]
                stack.pop()
            sums = c*arr[i] + stack[-1][2]
            stack.append((arr[i] , c, sums))
            ans = ans + sums
        return  ans

        
            