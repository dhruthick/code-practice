class Solution:
    '''
    EASY: 252
    Given an array of meeting time intervals where intervals[i] = [starti, endi], 
    determine if a person could attend all meetings.
    '''
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # time - O(nlogn), space - O(n) (sorting)
        intervals.sort(key = lambda x : x[1])
        last_end = - float('inf')
        for start, end in intervals:
            if start < last_end:
                return False
            last_end = end
        return True