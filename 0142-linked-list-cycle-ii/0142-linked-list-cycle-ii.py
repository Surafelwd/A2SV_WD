# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if  not  head  or not head.next:
            return None
        fast = head
        slow =head
        while fast.next:
            fast = fast.next.next
            slow = slow.next
            if  fast == slow :
                break
        else:
            return None
        while slow != head:
            slow = slow.next
            head = head.next
        return slow
        