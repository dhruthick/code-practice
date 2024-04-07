class Solution(object):
    '''
    MEDIUM: 1288

    Given an array intervals where intervals[i] = [li, ri] represent the 
    interval [li, ri), remove all intervals that are covered by another interval in the list.

    The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.

    Return the number of remaining intervals.
    '''
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        ans = 1
        intervals.sort(key = lambda x: (x[0], -x[1]))
        prev_end = intervals[0][1]
        for start, end in intervals:
            if end > prev_end:
                ans += 1
                prev_end = end
        return ans