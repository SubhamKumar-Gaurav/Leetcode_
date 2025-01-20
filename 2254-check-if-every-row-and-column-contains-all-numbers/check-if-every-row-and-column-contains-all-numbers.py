class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool: 
        def all_num(arr) : 
            n=len(arr) 
            for i in range(1,n+1) : 
                if i not in arr : 
                    return False 
            return True 

        for i in range(len(matrix)) :   # row check 
            if all_num(matrix[i])==False : 
                return False 
        
        for i in range(len(matrix)) : 
            temp=[]
            for j in range(len(matrix)) : 
                temp.append(matrix[j][i]) 
            if all_num(temp)==False : 
                return False 
        return True 