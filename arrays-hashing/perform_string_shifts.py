class Solution:
    '''
    EASY: 1427
    You are given a string s containing lowercase English letters, and a 
    matrix shift, where shift[i] = [directioni, amounti]:

        directioni can be 0 (for left shift) or 1 (for right shift).

        amounti is the amount by which string s is to be shifted.

        A left shift by 1 means remove the first character of s and 
        append it to the end.
        
        Similarly, a right shift by 1 means remove the last character 
        of s and add it to the beginning.

    Return the final string after all operations.
    '''
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        n = len(s)
        start = 0
        for direction, amount in shift:
            if direction == 0:
                start = (start + amount) % n
            else:
                start = (start - amount) % n
        return s[start:] + s[:start]