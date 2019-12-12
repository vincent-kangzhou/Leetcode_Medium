class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1=len(nums1)
        len2=len(nums2)
        
        if (len1+len2)%2:
            return self.findKth(nums1,nums2,(len1+len2)//2+1)
        
        else:
            return (self.findKth(nums1, nums2, (len1+len2)//2)+self.findKth(nums1, nums2,(len1+len2)//2+1))*0.5
        
        
   
    def findKth(self, num1, num2, k):
        len1=len(num1)
        len2=len(num2)
        
        if len1>len2: return self.findKth(num2, num1, k)
        
        if len1==0:
            return num2[k-1]
        if k==1: return min(num1[0], num2[0])
        
        pa=k//2
        
        pk=min(pa, len1)
        
        if num1[pk-1]<num2[pk-1]:
            return self.findKth(num1[pk:], num2, k-pk)
        else:
            return self.findKth(num1, num2[pk:],k-pk)
