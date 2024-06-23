class Solution:
    '''
    MEDIUM: 253
    Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], 
    return the minimum number of conference rooms required.
    '''
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # use min heap to keep track of rooms
        from heapq import heappush, heappop
        if not intervals:
            return 0
        free_rooms = []
        intervals.sort(key = lambda x: x[0])
        heappush(free_rooms, intervals[0][1])
        for i in intervals[1:]:
            if free_rooms[0] <= i[0]:
                heappop(free_rooms)
            heappush(free_rooms, i[1])
        return len(free_rooms)