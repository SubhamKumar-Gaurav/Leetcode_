class Solution: 
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        items=items1+items2 
        items.sort() 
        n=len(items) 
        arr=[[items[0][0], items[0][1]]] 
        for i in range(1, n) : 
            if items[i][0]==arr[-1][0] : 
                arr[-1][1]+=items[i][1] 
            else : 
                arr.append([items[i][0], items[i][1]]) 
        return arr 