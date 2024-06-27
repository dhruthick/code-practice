class TimeMap:
    '''
    MEDIUM: 981
    Design a time-based key-value data structure that can store multiple values 
    for the same key at different time stamps and retrieve the key's value at a 
    certain timestamp.

    Implement the TimeMap class:

    - TimeMap() Initializes the object of the data structure.
    - void set(String key, String value, int timestamp) Stores the key key with the 
    value value at the given time timestamp.
    - String get(String key, int timestamp) Returns a value such that set was called 
    previously, with timestamp_prev <= timestamp. If there are multiple such values, 
    it returns the value associated with the largest timestamp_prev. If there are 
    no values, it returns "".
    '''
    def __init__(self):
        self.key_time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # If the 'key' does not exist in dictionary.
        if not key in self.key_time_map:
            self.key_time_map[key] = []
            
        # Store '(timestamp, value)' pair in 'key' bucket.
        self.key_time_map[key].append([ timestamp, value ])
        

    def get(self, key: str, timestamp: int) -> str:
        # If the 'key' does not exist in dictionary we will return empty string.
        if not key in self.key_time_map:
            return ""
        
        if timestamp < self.key_time_map[key][0][0]:
            return ""
        
        left = 0
        right = len(self.key_time_map[key])
        
        while left < right:
            mid = (left + right) // 2
            if self.key_time_map[key][mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid

        # If iterator points to first element it means, no time <= timestamp exists.
        return "" if right == 0 else self.key_time_map[key][right - 1][1]