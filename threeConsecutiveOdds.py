class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        for i in range(0, len(arr)):
            if arr[i] % 2 == 0:
                count = 0
            else:
                count += 1
                if count >= 3: return True
            print("index: " + str(i) + ", value: " + str(arr[i]) + ", count:"  + str(count))
        return False
