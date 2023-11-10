class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = list()
        hash_t = {key: -1 for key in nums1}
        for x in nums2:
            while len(stack) > 0 and x > stack[-1]:
                if stack[-1] in hash_t:
                    hash_t[stack[-1]] = x
                stack.pop()
            stack.append(x)
        return [hash_t[x] for x in nums1]