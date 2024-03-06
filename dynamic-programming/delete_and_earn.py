class Solution(object):
    '''
    740: MEDIUM
    You are given an integer array nums.
    You want to maximize the number of points
    you get by performing the following 
    operation any number of times:

    Pick any nums[i] and delete it to earn 
    nums[i] points. Afterwards, you must 
    delete every element equal to nums[i] - 1 
    and every element equal to nums[i] + 1.

    Return the maximum number of points you 
    can earn by applying the above operation 
    some number of times.
    '''
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
        for i in count:
            count[i] *= i
        mem = {}
        def maxPoints(n):
            if n == 0:
                return 0
            if n == 1:
                return count[n]
            if n not in mem:
                mem[n] = max(count[n] + maxPoints(n - 2), maxPoints(n - 1))
            return mem[n]
        return maxPoints(max(nums))