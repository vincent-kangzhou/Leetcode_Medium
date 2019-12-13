class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right=0, len(height)-1
        ans=0
        
        while left < right:
            ans=max(ans, min(height[right], height[left])*(right-left))
            
            if height[right]<height[left]:
                right-=1
            else:
                left+=1
        return ans
