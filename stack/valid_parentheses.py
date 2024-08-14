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
        # time - O(n), space - O(n)
        stack = []
        bracket_map = {'{':'}','[':']','(':')'}
        for bracket in s:
            if bracket in ['{','[','(']:
                stack.append(bracket)
            elif not stack or bracket_map[stack.pop()] != bracket:
                return False
        return not stack