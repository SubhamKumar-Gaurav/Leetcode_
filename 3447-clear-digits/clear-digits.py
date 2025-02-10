class Solution:
    def clearDigits(self, s: str) -> str:
        res=[]
        del_cnt=0 
        for i in reversed(range(len(s))) : 
            if s[i].isdigit() : 
                del_cnt+=1 
            elif del_cnt : 
                del_cnt-=1 
            else : 
                res.append(s[i]) 
        return "".join(res[::-1])