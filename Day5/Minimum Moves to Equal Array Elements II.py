class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        mid=len(nums)//2
        count=0
        for i in range(0,mid):
            count+=nums[mid]-nums[i]
        for i in range(mid+1,len(nums)):
            count+=abs(nums[mid]-nums[i])
        return count
