class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # n jobs, m workers
        # 3 arrays: difficulty, profit, worker
        # difficulty[i] & profit[i] are difficulty & profit of ith job
        # worker[j] is ability of jth worker (jth worker can only complete a job with difficulty at most worker[j])
        # # return max profit we can achieve after assigning workers to jobs

        '''
        Ex.
        Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
        Output: 100
        Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get a profit of [20,20,30,30] separately
        '''
        total_profit = 0
        print("Difficulty: " + str(difficulty) + " and Profit: " + str(profit))
        for i in range(0, len(worker)):
            for j in range(len(difficulty)-1, -1, -1):
                if difficulty[j] <= worker[i]:
                    total_profit += profit[j]
                    print(total_profit)
                    break
        return total_profit 
