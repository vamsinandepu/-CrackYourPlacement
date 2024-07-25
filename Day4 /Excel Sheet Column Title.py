class Solution:
    def convertToTitle(self, n: int) -> str:
        str1=""
        while(n>0):
            n-=1
            x=n%26
            str1+=chr(65+x)
            n=n//26
        return str1[::-1]
