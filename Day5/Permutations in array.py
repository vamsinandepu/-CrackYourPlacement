class Solution:
    def isPossible(self,a, b, n, k):
    # Your code goes here
        a.sort(reverse=True)
        b.sort()
        for i in range(len(a)):
            if a[i]+b[i]<k:
                return False
        return True
