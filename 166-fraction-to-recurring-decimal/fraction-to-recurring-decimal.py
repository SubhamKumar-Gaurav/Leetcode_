
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str: 
        if numerator==0 : 
            return "0" 

        res=[]
        if (numerator*denominator) < 0 : 
            res.append("-") 
        
        num=abs(numerator)
        den=abs(denominator)
        res.append(str(num//den))  
        remain=num%den 
        if remain==0 : 
            return "".join(res)
        
        res.append(".") 
        mp={} 
        while remain!=0 : 
            if remain in mp : 
                res.insert(mp[remain], "(")
                res.append(")")  
                break 
            
            mp[remain]=len(res) 
            remain*=10 
            digit=remain//den 
            res.append(str(digit)) 
            remain=remain%den 

        return "".join(res) 