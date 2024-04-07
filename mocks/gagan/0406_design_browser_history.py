class BrowserHistory(object):
    '''
    MEDIUM: 1472
    You have a browser of one tab where you start on the homepage and you 
    can visit another url, get back in the history number of steps or move 
    forward in the history number of steps.

    Implement the BrowserHistory class:

    - BrowserHistory(string homepage) Initializes the object with the homepage 
    of the browser.
    - void visit(string url) Visits url from the current page. It clears up all 
    the forward history.
    - string back(int steps) Move steps back in history. If you can only return x 
    steps in the history and steps > x, you will return only x steps. Return the 
    current url after moving back in history at most steps.
    - string forward(int steps) Move steps forward in history. If you can only 
    forward x steps in the history and steps > x, you will forward only x steps. 
    Return the current url after forwarding in history at most steps.
    '''
    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.back_stack = []
        self.forward_stack = []
        self.current = homepage

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        self.back_stack.append(self.current)
        self.current = url
        self.forward_stack = []
        

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        for i in range(min(steps, len(self.back_stack))):
            self.forward_stack.append(self.current)
            self.current = self.back_stack.pop()
        return self.current

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        for i in range(min(steps, len(self.forward_stack))):
            self.back_stack.append(self.current)
            self.current = self.forward_stack.pop()
        return self.current
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)