class MovingAverage:
    '''
    EASY: 346
    Given a stream of integers and a window size, calculate the 
    moving average of all integers in the sliding window.

    Implement the MovingAverage class:

    - MovingAverage(int size) Initializes the object with the 
    size of the window size.
    - double next(int val) Returns the moving average of the 
    last size values of the stream.
    '''

    def __init__(self, size: int):
        self.size = size
        self.queue = []
        self.total = 0
        

    def next(self, val: int) -> float:
        if len(self.queue) == self.size:
            self.total -= self.queue.pop(0)
        self.total += val
        self.queue.append(val)

        return self.total/len(self.queue)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)