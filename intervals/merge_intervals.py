class Solution:
    '''
    MEDIUM: 56
    Given an array of intervals where intervals[i] = [starti, endi], 
    merge all overlapping intervals, and return an array of the 
    non-overlapping intervals that cover all the intervals in the 
    input.
    '''
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []
        n, i = len(intervals), 0
        curr = intervals[0]
        while i < n - 1:
            # if overlapping, merge
            if curr[0] <= intervals[i + 1][1] and curr[1] >= intervals[i + 1][0]:
                curr[0] = min(curr[0], intervals[i + 1][0])
                curr[1] = max(curr[1], intervals[i + 1][1])
                i += 1
            # otherwise append, and move on
            else:
                result.append(curr)
                curr = intervals[i + 1]
                i += 1
        result.append(curr)
        return result