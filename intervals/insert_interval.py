class Solution:
    '''
    MEDIUM: 57
    You are given an array of non-overlapping intervals intervals where 
    intervals[i] = [starti, endi] represent the start and the end of the 
    ith interval and intervals is sorted in ascending order by starti. 
    You are also given an interval newInterval = [start, end] that 
    represents the start and end of another interval.

    Insert newInterval into intervals such that intervals is still sorted 
    in ascending order by starti and intervals still does not have any 
    overlapping intervals (merge overlapping intervals if necessary).

    Return intervals after the insertion.

    Note that you don't need to modify intervals in-place. You can make 
    a new array and return it.
    '''
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        answer = []
        new_start, new_end = newInterval[0], newInterval[1]
        n, i = len(intervals), 0
        while i < n and intervals[i][1] < new_start:
            answer.append(intervals[i])
            i += 1
        # compare starting of current interval with end of new, vice-versa won't work
        while i < n and intervals[i][0] <= new_end:
            new_start = min(intervals[i][0], new_start)
            new_end = max(intervals[i][1], new_end)
            i += 1
        answer.append([new_start, new_end])
        while i < n:
            answer.append(intervals[i])
            i += 1
        return answer