
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]: 
        maxCharFreq=[0]*26
        tempCharFreq=[0]*26 

        for word in words2 : 
            for ch in word : 
                tempCharFreq[ord(ch)-ord('a')]+=1 
            for i in range(26) : 
                maxCharFreq[i]=max(maxCharFreq[i], tempCharFreq[i]) 
            tempCharFreq=[0]*26 
        
        res=[]
        for word in words1 : 
            for ch in word : 
                tempCharFreq[ord(ch)-ord('a')]+=1 
            flag=True 
            for i in range(26) : 
                if maxCharFreq[i]>tempCharFreq[i] : 
                    flag=False 
                    break 
            if flag : 
                res.append(word) 
            tempCharFreq=[0]*26
        return res