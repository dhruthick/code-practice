class Solution:
    '''
    HARD: 1335
    You want to schedule a list of jobs in d days. Jobs are dependent 
    (i.e To work on the ith job, you have to finish all the jobs j where 0 <= j < i).

    You have to finish at least one task every day. The difficulty of a job schedule is 
    the sum of difficulties of each day of the d days. The difficulty of a day is the 
    maximum difficulty of a job done on that day.

    You are given an integer array jobDifficulty and an integer d. The difficulty of 
    the ith job is jobDifficulty[i].

    Return the minimum difficulty of a job schedule. If you cannot find a schedule for 
    the jobs return -1.
    '''
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        # If we cannot schedule at least one job per day, 
        # it is impossible to create a schedule
        if n < d:
            return -1
        
        hardest_job_remaining = [0] * n
        hardest_job = 0
        for i in range(n - 1, -1, -1):
            hardest_job = max(hardest_job, jobDifficulty[i])
            hardest_job_remaining[i] = hardest_job
        
        @lru_cache(None)
        def dp(i, day):
            # Base case, it's the last day so we need to finish all the jobs
            if day == d:
                return hardest_job_remaining[i]
            
            best = float("inf")
            hardest = 0
            # Iterate through the options and choose the best
            for j in range(i, n - (d - day)): # Leave at least 1 job per remaining day
                hardest = max(hardest, jobDifficulty[j])
                best = min(best, hardest + dp(j + 1, day + 1)) # Recurrence relation

            return best
        
        return dp(0, 1)