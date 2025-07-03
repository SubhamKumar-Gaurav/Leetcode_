
class Solution: 
    def partitionString(self, s: str) -> List[str]: 
        seen=set() 
        arr=[]
        curr=""
        for i in range(len(s)) : 
            curr+=s[i] 
            if curr not in seen : 
                arr.append(curr) 
                seen.add(curr) 
                curr="" 
        return arr 