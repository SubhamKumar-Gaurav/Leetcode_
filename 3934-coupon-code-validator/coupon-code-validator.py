class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]: 
        allowed={"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9","_", "electronics", "grocery", "pharmacy", "restaurant"} 
        
        n=len(code)
        arr=[] 
        for i in range(n) : 
            if isActive[i] and len(code[i])>0 :
                for j in code[i] : 
                    if j not in allowed : 
                        break
                else : 
                    if businessLine[i] in allowed : 
                        arr.append([code[i], businessLine[i]]) 
        arr.sort(key=lambda x: (x[1], x[0])) 
        
        res=[] 
        for i, j in arr : 
            res.append(i) 
        return res 