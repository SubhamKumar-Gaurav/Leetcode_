class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1=list(num1)[::-1] 
        num2=list(num2)[::-1] 
        res=0 
        for i in range(len(num1)) : 
            temp=0 
            for j in range(len(num2)) : 
                temp+=(int(num1[i])*int(num2[j]))*pow(10,j) 
            temp=temp*pow(10,i) 
            res+=temp
        return str(res)