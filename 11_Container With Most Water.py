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

    
    
    
    class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right=0, len(height)-1
        res=0
        while left<right:
            water=min(height[right], height[left])*(right-left)
            if res<water:
                res=water
                
            if height[left]>height[right]:
                cur=height[right]
                right-=1
                while left<right and height[right]<cur:
                    right-=1
                    
            else:
                cur=height[left]
                left+=1
                while left<right and height[left]<cur:
                    left+=1
                    
        return res
        
