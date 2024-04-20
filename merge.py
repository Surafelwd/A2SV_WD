class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        l=m-1
        r=n-1
        i=n+m-1
        
        while l >=0 and r>=0:
            if nums1[l] > nums2[r]:
                nums1[i]=nums1[l]
                l-=1
            else:
                nums1[i]=nums2[r]
                r-=1
            i-=1
        while r>=0:
            nums1[i]=nums2[r]
            r-=1
            i-=1
        return nums1
