class Solution:
    def reverseWords(self, s: str) -> str:
        str1=""
        l=s.split()
        l.reverse()
        return " ".join(l)
