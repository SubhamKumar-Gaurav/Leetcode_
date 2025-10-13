class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        i="".join(sorted(s)) 
        j="".join(sorted(t))
        return i==j 