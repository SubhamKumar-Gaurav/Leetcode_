
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str: 
        newString=part+"#"+s 
        freqArray=[0 for _ in range(len(newString))] 
        ans=[] 
        n=len(part) 
        length=0 
        i=1 
        while i<len(newString) : 
            if newString[i]==newString[length] : 
                length+=1 
                freqArray[i]=length 
                if i>n : 
                    ans.append((newString[i], length)) 
                if length==n : 
                    for _ in range(n) : 
                        ans.pop() 
                    if not ans : 
                        length=0 
                    else : 
                        length=ans[-1][-1] 
            else : 
                if length>0 : 
                    length=freqArray[length-1] 
                    i-=1 
                else : 
                    freqArray[i]=0 
                    if i>n : 
                        ans.append((newString[i], 0))
            i+=1 
        return "".join(i[0] for i in ans) 