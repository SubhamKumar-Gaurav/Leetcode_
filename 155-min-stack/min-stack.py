class MinStack:

    def __init__(self):
        self.stack=[] 
        self.minEle=None 

    def push(self, val: int) -> None:
        if len(self.stack)<1 : 
            self.stack.append(val) 
            self.minEle=val 
        else : 
            if val>=self.minEle : 
                self.stack.append(val) 
            else : 
                self.stack.append(2*val-self.minEle) 
                self.minEle=val


    def pop(self) -> None: 
        y=self.stack.pop() 
        if y<self.minEle : 
            self.minEle=(2*self.minEle)-y 
         
        
    def top(self) -> int:
        x=self.stack[-1] 
        if x>=self.minEle : 
            return x 
        else : 
            return self.minEle 

    def getMin(self) -> int:
        return self.minEle 


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()