class Solution(object):
    '''
    MEDIUM: 739
    Given an array of integers temperatures represents the daily temperatures, 
    return an array answer such that answer[i] is the number of days you have 
    to wait after the ith day to get a warmer temperature. If there is no future 
    day for which this is possible, keep answer[i] == 0 instead.
    '''
    def dailyTemperatures(self, temperatures):
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([t,i])
        return res
        