# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return head
        while head.val == val:
            head = head.next
            if head is None:
                return None
        prev = head
        node = head.next
        while node:
            if node.val == val:
                node = node.next
                prev.next = node
                continue
            prev = node
            node = prev.next
        return head
