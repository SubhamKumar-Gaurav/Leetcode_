class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        d={} 
        for i in nums1 : 
            d[i[0]]=i[1]  
        for i in nums2 :
            if i[0] in d :
                d[i[0]]+=i[1] 
            else :
                d[i[0]]=i[1]
        arr=[]  
        for i in d : 
            arr.append([i, d[i]])
        arr.sort(key=lambda x: x[0])
        return arr