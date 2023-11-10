def twoSum(self, nums, target):
    diffs = dict()
    for i in range(len(nums)):
        diffs[nums[i]] = i
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in diffs.keys() and diffs[diff] != i:
            return i, diffs[target - nums[i]]
