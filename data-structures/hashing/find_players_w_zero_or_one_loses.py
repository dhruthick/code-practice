class Solution:
    '''
    MEDIUM: 2225
    You are given an integer array matches where matches[i] = [winneri, loseri] 
    \indicates that the player winneri defeated player loseri in a match.

    Return a list answer of size 2 where:

    - answer[0] is a list of all players that have not lost any matches.
    - answer[1] is a list of all players that have lost exactly one match.

    The values in the two lists should be returned in increasing order.

    Note:

    You should only consider the players that have played at least one match.
    The testcases will be generated such that no two matches will have the same outcome.

    '''
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict

        loses = defaultdict(int)

        for winner, loser in matches:
            loses[winner] = loses[winner]
            loses[loser] += 1
        
        answer0 = sorted([w for w in loses if loses[w] == 0])
        answer1 = sorted([l for l in loses if loses[l] == 1])

        return [answer0, answer1]
