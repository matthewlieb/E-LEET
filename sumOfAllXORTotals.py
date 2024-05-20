class Solution:
    import itertools
    def subsetXORSum(self, nums: List[int]) -> int:
        # initialize XOR total
        sum = 0
        # loop through list and produce all possible combinations
        for num in range(len(nums)+1):
            for subset in itertools.combinations(nums, num):
                # print current combination
                print(list(subset))
                # reduce the combinations with bitwise XOR
                if subset:
                    # add bitwise XOR to sum
                    sum += reduce(lambda x, y: x ^ y, list(subset))
        # return sum
        return sum
