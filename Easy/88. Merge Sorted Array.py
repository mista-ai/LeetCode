class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pos1 = m-1
        pos2 = n-1
        write_index = m + n - 1

        while pos2 >= 0:
          if pos1 >= 0 and nums1[pos1] > nums2[pos2]:
            nums1[write_index] = nums1[pos1]
            pos1 -= 1
          else:
            nums1[write_index] = nums2[pos2]
            pos2 -= 1

          write_index -= 1