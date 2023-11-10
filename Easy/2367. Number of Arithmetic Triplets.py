class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        num_dict = dict()
        for x in nums:
            num_dict[x] = (x + diff, x + diff * 2)
        counter = 0
        for key, val in num_dict.items():
            if val[0] in num_dict and val[1] in num_dict:
                counter += 1
        return counter