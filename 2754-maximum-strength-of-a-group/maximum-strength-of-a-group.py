class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        n=len(nums)
        negative=[] 
        positive=[] 
        zero=[]  
        for i in range(n) : 
            if nums[i]<0 : 
                negative.append(nums[i]) 
            elif nums[i]>0 : 
                positive.append(nums[i]) 
            else : 
                zero.append(nums[i]) 

        if len(positive)>0 : 
            pos=1 
            for i in positive : 
                pos*=i 
        else : 
            pos=None 

        if len(zero)>0 : 
            z=0 
        else : 
            z=None 

        if len(negative)>0 : 
            neg=1 
            if len(negative)==1 : 
                if pos is None and z is None : 
                    return negative[0] 
                if pos is None and z is not None :
                    return z 
                if pos is not None and z is None : 
                    neg=None 
            else :
                neg=1 
                negative.sort() 
                for i in range(0, len(negative)-1, 2) : 
                    neg=neg*negative[i]*negative[i+1] 
        else : 
            neg=None     
        
        if pos is None and (neg is None or len(negative)==1) and z is not None : 
            return z 
        res=1 
        if pos is not None : 
            res=res*pos 
        if neg is not None : 
            res=res*neg 
        if pos is None and z is not None and neg is None : 
            res=res*z 

        return res 
        
