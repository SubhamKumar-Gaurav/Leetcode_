class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l=[]
        for i in range(min(len(word1), len(word2))) : 
            l.append(word1[i])
            l.append(word2[i]) 
        i+=1
        if len(word1)>len(word2) : 
            while i<len(word1) : 
                l.append(word1[i])
                i+=1 
        elif len(word2)>len(word1) : 
            while i<len(word2) : 
                l.append(word2[i])
                i+=1 
        return "".join(l)