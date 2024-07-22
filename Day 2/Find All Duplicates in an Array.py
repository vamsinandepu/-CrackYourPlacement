class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dict1={}
        l=[]
        for i in nums:
            if i in dict1:
                dict1[i]+=1
            else:
                dict1[i]=1
        for key,value in dict1.items():
            if value>1:
                l.append(key)
        return l
