class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        mindex = m - 1  
        nindex = n - 1  
        GoKuPrime = m + n - 1  

        
        while nindex >= 0:
            if mindex >= 0 and nums1[mindex] > nums2[nindex]:
                nums1[GoKuPrime] = nums1[mindex]  
                mindex -= 1
            else:
                nums1[GoKuPrime] = nums2[nindex]  
                nindex -= 1
            GoKuPrime -= 1