class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # change s to t
        # |s[i] - t[i]|
        # return max length of substring s that can be changed to be same as t without > maxCost

        # initialize array cost to store difference between s and t
        cost = [0] * len(s)

        # iterate through substrings of s using i and j to calculate sum of costs in substring s[i:j]
        result, i, costSum = 0, 0, 0

        # calculate sum of costs in substring
        for j in range(len(s)):
            costSum += abs(ord(s[j]) - ord(t[j]))

        # if costSum exceeds maxCost, move i to the right until costSum does not exceed maxCost
            while costSum > maxCost:
                costSum -= abs(ord(s[i]) - ord(t[i]))
                i += 1

            result = max(result, (j-i)+1)

        # return the result with max length of substrings
        return result
        
