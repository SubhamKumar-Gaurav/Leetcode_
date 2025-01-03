class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m=len(nums1)
        n=len(nums2)
        sorted_arr=[] 
        i=0 
        j=0 
        while i<m and j<n : 
            if nums1[i]<nums2[j] : 
                sorted_arr.append(nums1[i]) 
                i+=1 
            else : 
                sorted_arr.append(nums2[j]) 
                j+=1 
        while i<m : 
            sorted_arr.append(nums1[i])
            i+=1 
        while j<n : 
            sorted_arr.append(nums2[j]) 
            j+=1 

        if (m+n)%2==1 : 
            return sorted_arr[(m+n)//2] 
        else : 
            return (sorted_arr[(m+n)//2]+sorted_arr[(m+n)//2-1])/2