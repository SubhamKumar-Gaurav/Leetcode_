
class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]: 
        res=[] 
        x=0 
        for i in range(len(word)) :  
            x=(x*10)+int(word[i])
            if x%m : 
                res.append(0) 
            else : 
                res.append(1)
            x=x%m  
        return res 