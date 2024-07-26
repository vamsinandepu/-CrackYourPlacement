from typing import List
class Solution:
    def findPair(self, n : int, x : int, arr : List[int]) -> int:
        # code here
        arr.sort()
        i,j=0,1
        while(i<n and j<n):
            if i!=j and arr[j]-arr[i]==x:
                return 1
            elif arr[j]-arr[i]<x:
                j+=1
            else:
                i+=1
        return -1
