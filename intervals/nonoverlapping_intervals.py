class Solution:
    '''
    MEDIUM: 435
    Given an array of intervals intervals where intervals[i] = [starti, endi], 
    return the minimum number of intervals you need to remove to make the rest 
    of the intervals non-overlapping.
    '''
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by end of intervals
        intervals.sort(key = lambda x: x[1])
        count = 0
        last_end = - float('inf')
        for start, end in intervals:
            # keep if not overlapping with the last interval
            if start >= last_end:
                last_end = end
            else:
                count += 1 
        return count