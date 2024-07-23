class Solution:
    def maxScore(self, nums: List[int], k: int) -> int:
        left=sum(nums[0:k])
        right=0
        j=-1
        count=left+right
        max1=count
        for i in range(k-1,-1,-1):
            left-=nums[i]
            right+=nums[j]
            j-=1
            count=left+right
            max1=max(max1,count)
        return max1
