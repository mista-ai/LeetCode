from collections import defaultdict
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hash_table = defaultdict(int)
        prev = head
        cur = prev
        while cur:
            if cur.val in hash_table:
                prev.next = cur.next
                cur = prev.next
                continue
            hash_table[cur.val] += 1
            prev = cur
            cur = cur.next
        return head