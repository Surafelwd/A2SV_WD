# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        prev = node

        while prev.next:
            prev.val = prev.next.val
            if prev.next.next is None:
                prev.next = None
                break
            prev = prev.next
        