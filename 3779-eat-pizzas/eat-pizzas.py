class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        pizzas.sort(reverse=True) 
        num=len(pizzas)//4 
        if num%2==1 : 
            even=num//2 
            odd=num-even 
            res=0 
            for i in range(odd) : 
                res+=pizzas[i] 
            i=odd+1 
            while even>0 : 
                res+=pizzas[i]
                i+=2 
                even-=1
            return res 

        else : 
            odd=num//2 
            even=num//2 
            res=0 
            for i in range(odd) : 
                res+=pizzas[i] 
            i=odd+1 
            while even>0 : 
                res+=pizzas[i]
                i+=2 
                even-=1 
            return res 