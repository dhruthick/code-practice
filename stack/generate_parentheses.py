class Solution:
    '''
    MEDIUM: 22
    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
    '''
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backTrack(open, closed):
            if open == closed == n:
                res.append("".join(stack))
                return

            if open < n:
                stack.append("(")
                backTrack(open + 1, closed)
                stack.pop()

            if closed < open:
                stack.append(")")
                backTrack(open, closed + 1)
                stack.pop()

        backTrack(0,0)

        return res