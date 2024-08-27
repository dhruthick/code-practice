'''Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1
'''
def firstUniqChar(s: str) -> int:
    count = {}
    for c in s:
        count[c] = 1 + count.get(c, 0)
    #print(count)
    char = None
    for k, v in count.items():
        if v == 1:
            return s.index(k)
    return -1

assert firstUniqChar('leetcode') == 0
assert firstUniqChar('loveleetcode') == 2
assert firstUniqChar('aabb') == -1