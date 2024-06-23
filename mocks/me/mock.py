class Dice:
    @lru_cache(None)
    def backtrack(self, throw_count, sum_so_far):
        if throw_count == self.num_throws:
            if sum_so_far > self.target:
                return 1
            else:
                return 0
        num_ways = 0
        for i in range(1, 7):
            num_ways += self.backtrack(throw_count + 1, sum_so_far + i)
        return num_ways


    def sumProbability(self, num_throws, target):
        self.num_throws = num_throws
        self.target = target

        return self.backtrack(0, 0) / (6 ** self.num_throws)