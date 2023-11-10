from collections import defaultdict, deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        nums = defaultdict(int)
        search = deque([root])
        max_count = 0
        while search:
            v = search.popleft()
            if v:
                nums[v.val] += 1
                if nums[v.val] > max_count:
                    max_count = nums[v.val]
                search.append(v.left)
                search.append(v.right)
        result = list()
        for k, v in nums.items():
            if v == max_count:
                result.append(k)
        return result
