class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i=0
        j=0
        w=[]
        while i < len(nums1) and j<len(nums2):
            if nums1[i] > nums2[j]:
                j+=1
            elif nums1[i]==nums2[j]:
                w.append(nums1[i])
                j+=1
                i+=1
            else:
                i+=1
        if len(w)==0:
            return -1
        else:
            return(min(w))
                
