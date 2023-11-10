class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = sorted(set(nums1))
        nums2 = sorted(set(nums2))
        left = max(nums1[0], nums2[0])
        right = min(nums1[-1], nums2[-1])
        min_nums = nums1
        max_nums = nums2
        if len(min_nums) > len(max_nums):
            min_nums, max_nums = max_nums, min_nums
        min_nums = list(filter(lambda x: left <= x <= right, min_nums))
        max_nums = list(filter(lambda x: left <= x <= right, max_nums))
        start = 0
        result = list()
        for x in min_nums:
            end = len(max_nums) - 1
            while start <= end:
                mid = (start + end) // 2
                if max_nums[mid] == x:
                    result.append(x)
                    break
                elif max_nums[mid] < x:
                    start = mid + 1
                else:
                    end = mid - 1
        return result