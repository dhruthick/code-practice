class Solution(object):
    '''
    EASY: 1544

    Given a string s of lower and upper case English letters.
    
    A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:
    0 <= i <= s.length - 2
    s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
    To make the string good, you can choose two adjacent characters that make the string bad and 
    remove them. You can keep doing this until the string becomes good.

    Return the string after making it good. The answer is guaranteed to be unique under the given constraints.
    
    Notice that an empty string is also good.
    '''
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        # tried on array (check array and pointer) approach in O(n), didn't pass all the test cases.
        # later realised a stack would work better
        stack = []
        for char in s:
            if stack and char != stack[-1] and char.lower() == stack[-1].lower():
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)