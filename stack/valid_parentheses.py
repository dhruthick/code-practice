class Solution(object):
    '''
    20: EASY

    Given a string s containing just the
    characters '(', ')', '{', '}', '[' and ']', 
    determine if the input string is valid.
    '''
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        match = {
            '{':'}','[':']','(':')'
        }
        stack = []
        for b in s:
            if b in ['{','(','[']:
                stack.append(b)
            else:
                if len(stack) == 0 or match[stack.pop()] != b:
                    return False
        return not stack