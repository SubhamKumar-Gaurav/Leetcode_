
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n=len(s) 
        shift=[0]*(n+1) 
        for shiftOp in shifts : 
            start, end, direction = shiftOp 
            if direction==1 : 
                shift[start]+=1 
            else : 
                shift[start]-=1
            if end+1 < n : 
                if direction==1 : 
                    shift[end+1]-=1 
                else : 
                    shift[end+1]-= -1 
             
        currShift=0 
        shiftList=list(s) 
        for i in range(n) : 
            currShift+=shift[i] 
            netShift=(currShift%26 +26 )%26 
            shiftList[i]= chr((ord(shiftList[i])- ord('a')+netShift)%26 + ord('a')) 
        return ''.join(shiftList) 