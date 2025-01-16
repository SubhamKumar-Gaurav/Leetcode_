class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int: 
        if len(nums1)%2==0 and len(nums2)%2==0 : 
            return 0 
        elif len(nums1)%2 and len(nums2)%2 : 
            ans=nums1[0] 
            for i in range(1,len(nums1)) : 
                ans = ans^nums1[i] 
            for j in range(len(nums2)) : 
                ans = ans^nums2[j] 
            return ans
        elif len(nums1)%2  : 
            ans=nums2[0] 
            for i in range(1,len(nums2)) : 
                ans=ans^nums2[i]
            return ans 
        elif len(nums2)%2 : 
            ans=nums1[0] 
            for i in range(1,len(nums1)) : 
                ans = ans^nums1[i] 
            return ans