class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        dict1={}
        for i in nums:
            if i in dict1:
                dict1[i]+=1
            else:
                dict1[i]=1
        for key,values in dict1.items():
            if values>n//2:
                return key
            else:
                pass
