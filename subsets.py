class Solution:
    import itertools
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # initialize new list with all subsets
        subsets = []
        # for every number in subsets
        for num in range(len(nums)+1):
            # for every every subset combination of num in nums
            for subset in itertools.combinations(nums, num):
                # add current combination to list
                subsets.append(list(subset))
        return subsets
        
