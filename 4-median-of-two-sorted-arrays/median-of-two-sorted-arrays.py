class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float: 
        def bSearchMedian(arr) : 
            n=len(arr)
            if n%2==0 : 
                return (arr[n//2]+arr[n//2 - 1])/2
            return arr[n//2]

        n1=len(nums1) 
        n2=len(nums2) 

        # If one of the arrays is empty 
        if n1==0 and n2!=0 : 
            return bSearchMedian(nums2)
        if n1!=0 and n2==0 : 
            return bSearchMedian(nums1)

        if n2<n1 : 
            nums1, nums2 = nums2, nums1 
            n2, n1 = n1, n2
        
        b1=0 
        e1=n1

        while b1<=e1 : 
            i1=(b1+e1)//2 
            i2=(n1+n2+1)//2 - i1 
            mnr1=float("inf") if i1==n1 else nums1[i1]
            mxl1=float("-inf") if i1==0 else nums1[i1-1] 
            mnr2=float("inf") if i2==n2 else nums2[i2]
            mxl2=float("-inf") if i2==0 else nums2[i2-1]

            if mxl1<=mnr2 and mxl2<=mnr1 : 
                if (n1+n2)%2==0 : 
                    return (max(mxl1,mxl2)+min(mnr1,mnr2))/2 
                else : 
                    return max(mxl1,mxl2) 
            elif mxl1>mnr2 : 
                e1=i1-1 
            else : 
                b1=i1+1 
