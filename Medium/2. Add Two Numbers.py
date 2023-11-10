# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
            result = ListNode(0)
            head = result
            while True:
                if l1 is not None:
                    result.val += l1.val
                    l1 = l1.next
                if l2 is not None:
                    result.val += l2.val
                    l2 = l2.next
                next_val = 0
                if result.val > 9:
                    next_val = 1
                    result.val %= 10
                if l1 is None and l2 is None:
                    result.next = None
                    if next_val != 0:
                        result.next = ListNode(next_val)
                    break
                result.next = ListNode(next_val, result)
                result = result.next
            return head