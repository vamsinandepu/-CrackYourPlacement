from itertools import permutations
class Solution:
    def uniquePerms(self, arr, n):
        res=list(sorted(set(permutations(arr))))
        return res
