class Solution:
    from collections import Counter
    def singleNumber(self, nums: List[int]) -> List[int]:
        new_nums = []
        for val in nums:
            if nums.count(val) == 1 and val not in new_nums:
                new_nums.append(val)
        return new_nums
