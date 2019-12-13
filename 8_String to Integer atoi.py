class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        int_max=2**31-1
        int_min=(2**31)*-1
        str=str.strip()
        
        if str=='' : return 0
        sum=0
        sign=1
        start=0
        
        if not str[start].isdigit() and not str[start] in ["-",'+']:
            return 0
        
        
        if str[start]=='-':
            sign=-1
        
        if str[start]=='-' or str[start]=='+':
            start+=1
            
        res=''
        
        for j in range(start, len(str)):
            if str[j].isdigit():
                res+=str[j]
            else:
                break
        
        for i in range(len(res)):
            sum+=(int(res[i])*pow(10, len(res)-1-i))
        if sign==1:
            return min(int_max, sum)
        else:
            return max(int_min, sum*-1)
