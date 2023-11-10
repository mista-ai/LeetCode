class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        elem_dict = dict()
        result = list()
        for x in nums1:
            if x not in elem_dict:
                elem_dict[x] = 1
            else:
                elem_dict[x] += 1
        for x in nums2:
            if x in elem_dict and elem_dict[x] > 0:
                result.append(x)
                elem_dict[x] -= 1
        return result