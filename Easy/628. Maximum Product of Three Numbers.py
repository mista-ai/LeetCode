class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        smallest_two = [float("inf")] * 2
        biggest_three = [float("-inf")] * 3

        for num in nums:
            if num <= smallest_two[0]:
                smallest_two[0] = num
                smallest_two.sort(reverse=True)
            if num >= biggest_three[0]:
                biggest_three[0] = num
                biggest_three.sort()

        return max(smallest_two[0] * smallest_two[1] * biggest_three[2],
                   biggest_three[0] * biggest_three[1] * biggest_three[2])
