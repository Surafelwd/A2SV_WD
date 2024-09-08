# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        ans = []
        n=0
        cur = head
        while cur:
            n+=1
            cur =cur.next
        e = n//k
        e1 = n%k
        cur = head
        for i in range (k):
            newhead = cur
            size = e + (1 if e1 >0 else 0)
            e1 -=1
            for _ in range(size-1):
                if cur:
                    cur= cur.next
            if cur:
                nexthead = cur.next
                cur.next = None
                cur = nexthead
            ans.append(newhead)
        return ans


        