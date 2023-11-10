from collections import deque


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        direct = deque()
        reverse = deque()
        while head:
            direct.append(head.val)
            reverse.appendleft(head.val)
            head = head.next
        return direct == reverse
