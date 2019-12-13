class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows<=1: return s
        if len(s)<=numRows: return s
        
        arr=['']*(numRows)
        
        line=0
        step=-1
        for c in s:
            arr[line]+=c
            
            if line%(numRows-1)==0:
                step=-step
                
            line+=step
        return ''.join(arr)
