# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix=[[-1] * n for _ in range(m)]
        i , j,d = 0,0 ,0
        cur = head 
        ro = [(0,1), (1,0),(0,-1),(-1,0)]
        while cur:
            matrix[i][j] = cur.val
            cur = cur.next
            inext , jnext = i+ro[d%4][0],j+ro[d%4][1]
            if 0<= inext < m and 0<=jnext <n and matrix[inext][jnext]==-1:
                i, j = inext, jnext
            else:
                d+=1
                i ,j = i+ro[d%4][0],j+ro[d%4][1]
        return matrix