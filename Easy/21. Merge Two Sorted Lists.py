# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is not None:
            return ListNode(list2.val, self.mergeTwoLists(list1, list2.next))
        if list2 is None and list1 is not None:
            return ListNode(list1.val, self.mergeTwoLists(list1.next, list2))
        if list2 is None and list1 is None:
            return None
        if list1.val < list2.val:
            return ListNode(list1.val, self.mergeTwoLists(list1.next, list2))
        else:
            return ListNode(list2.val, self.mergeTwoLists(list2.next, list1))