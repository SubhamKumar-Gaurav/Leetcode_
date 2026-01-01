class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s="" 
        for i in digits : 
            s+=str(i) 
        
        ans=str(int(s)+1)
        arr=[] 
        for i in ans : 
            arr.append(int(i)) 
        return arr 