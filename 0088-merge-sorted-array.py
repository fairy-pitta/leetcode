class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        n1p = m-1 
        n2p = n-1
        endpoint = m+n-1

        while n2p >= 0:
            if n1p >= 0 and nums1[n1p] >= nums2[n2p]:
                nums1[endpoint] = nums1[n1p]
                n1p -= 1 
            else:
                nums1[endpoint] = nums2[n2p]
                n2p -= 1
            
            endpoint -= 1



        return