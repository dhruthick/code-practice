class Solution(object):
    '''
    MEDIUM: 46
    Given an array nums of distinct integers, return all the possible permutations. 
    You can return the answer in any order.
    '''
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answers=[]
        def backtrack(choices, answer):
            if len(answer)==len(nums):
                answers.append(answer)
                return
            for c in choices:
                n_choices=choices.copy()
                n_choices.remove(c)
                backtrack(n_choices,answer+[c])
        backtrack(set(nums),[])
        return answers