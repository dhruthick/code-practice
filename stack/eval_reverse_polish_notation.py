class Solution:
    '''
    MEDIUM: 150
    You are given an array of strings tokens that represents an arithmetic 
    expression in a Reverse Polish Notation.

    Evaluate the expression. Return an integer that represents the value of 
    the expression.

    Note that:

    The valid operators are '+', '-', '*', and '/'.
    Each operand may be an integer or another expression.
    The division between two integers always truncates toward zero.
    There will not be any division by zero.
    The input represents a valid arithmetic expression in a reverse polish notation.
    The answer and all the intermediate calculations can be represented in a 32-bit integer.
    '''
    def operate(self, operator, num1, num2):
        if operator == "+":
            return num1+num2
        elif operator == "-":
            return num1-num2
        elif operator == "*":
            return num1*num2
        elif operator == "/":
            return num1/num2

    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        operators = ("+", "-", "*", "/")

        for t in tokens:
            if t not in operators:
                stack.append(t)
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                res = self.operate(t, int(num1), int(num2))
                stack.append(res)
        
        return int(stack[-1])