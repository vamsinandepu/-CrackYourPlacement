class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        n=len(nums)
        l=[0]*n
        l[n-1]=nums[n-1]
        result=0
        for i in range(n-2,-1,-1):
            l[i]=max(l[i+1],nums[i])
        for i in range(n):
            result=max(result,l[i]-nums[i])
        return result
