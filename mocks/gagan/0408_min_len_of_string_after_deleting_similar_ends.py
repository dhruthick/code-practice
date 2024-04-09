class Solution:
    '''
    MEDIUM: 1750
    Given a string s consisting only of characters 'a', 'b', and 'c'. You are 
    asked to apply the following algorithm on the string any number of times:

        - Pick a non-empty prefix from the string s where all the characters in the prefix are equal.
        - Pick a non-empty suffix from the string s where all the characters in this suffix are equal.
        - The prefix and the suffix should not intersect at any index.
        - The characters from the prefix and suffix must be the same.
        - Delete both the prefix and the suffix.

    Return the minimum length of s after performing the above operation any 
    number of times (possibly zero times).
    '''
    def minimumLength(self, s: str) -> int:
        begin = 0
        end = len(s) - 1

        # Delete similar ends until the ends differ or they meet in the middle
        while begin < end and s[begin] == s[end]:
            c = s[begin]

            # Delete consecutive occurrences of c from prefix
            while begin <= end and s[begin] == c:
                begin += 1

            # Delete consecutive occurrences of c from suffix
            while end > begin and s[end] == c:
                end -= 1

        # Return the number of remaining characters
        return end - begin + 1