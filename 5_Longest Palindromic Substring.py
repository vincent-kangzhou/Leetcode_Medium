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
            
            
            
            
            
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length=len(s)
        if length==1:
            return s
        res=''
        for i in range(length):
            for j in range(i, length):
                if self.isPalindromic(s, i, j) and len(res)<(j-i+1):
                    res=s[i:j+1]          
        return res
                     
    def isPalindromic(self,string, start, end):
        while start<=end:
            if string[start]!=string[end]:
                return False
            else:
                start+=1
                end-=1
                
        return True
        
        
        
        
        
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        if len(s)==1:
            return s
        
        n=len(s)
        start, end, maxL=0,0,0
        
        dp=[[0]*n for _ in range(n)]
        
        for i in range(n):
            for j in range(i):
                dp[j][i]=(s[j]==s[i])&((i-j<2)|dp[j+1][i-1])
                
                if dp[j][i] and maxL<(i-j+1):
                    start=j
                    end=i
                    maxL=(i-j+1)
                    
            dp[i][i]=1
        return s[start: end+1]
