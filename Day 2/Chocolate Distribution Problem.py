class Solution:
    def findMinDiff(self, a,n,m):      
        i=0
        j=m-1
        a.sort()
        l=[]
        while(j<n):
            x=a[j]-a[i]
            l.append(x)
            i+=1
            j+=1
        return min(l)
