class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        List1=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    l=[]
                    if(nums[i]+nums[j]+nums[k]==0):
                        if(i!=j and i!=k and j!=k):
                            l.append(nums[i])
                            l.append(nums[j])
                            l.append(nums[k])
                            l.sort()
                            List1.append(l)
        for i in range(len(List1)-1):
            for j in range(i+1,len(List1)):
                if(List1[i]==List1[j]):
                    List1.remove(List1[j])      
        return List1
