class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        s=set(brokenLetters) 
        l=list(text.split(" ")) 
        ans=len(l) 
        for i in l : 
            for j in s : 
                if j in i : 
                    ans-=1 
                    break 
        return ans