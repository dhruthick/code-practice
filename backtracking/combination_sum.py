class Solution:
    '''
    39: MEDIUM
    Given an array of distinct integers candidates 
    and a target integer target, return a list of 
    all unique combinations of candidates where the 
    chosen numbers sum to target. You may return 
    the combinations in any order.
    
    The same number may be chosen from candidates
    an unlimited number of times. Two combinations 
    are unique if the frequency of at least one of 
    the chosen numbers is different.
    '''
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # n - number of candidates, t - target, m - minimal value candidate
        # time - O(n^(t/m + 1)), n-ary tree with height t/m
        # space - O(t/m)

        def find_combinations(combination, sum_left, start):
            if sum_left == 0:
                nonlocal answer
                answer.append(combination)
                return
            if sum_left < 0:
                return
            # pick all you want of the number now. no backsies.
            for i in range(start, len(candidates)):
                find_combinations(combination + [candidates[i]], sum_left - candidates[i], i)
        answer = []
        find_combinations([], target, 0)

        return answer