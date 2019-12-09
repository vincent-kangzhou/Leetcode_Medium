class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        int1,int2=0,0
        
        len1=len(num1)
        len2=len(num2)
        for i in range(len1-1,-1,-1):
            int1+=(ord(num1[i])-48)*(10**(len1-1-i))
            
        for i in range(len2-1,-1,-1):
            int2+=(ord(num2[i])-48)*(10**(len2-1-i))
            
        res=int1*int2
        
        
        str1=''
        while res:
            str1+=chr(res%10+48)
            res//=10
        
        return str1[::-1] if len(str1)>0 else '0'
        
        
        
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        num1_=num1[::-1]
        num2_=num2[::-1]
        
        res=[0]*(len(num1_)+len(num2_))
        
        for i in range(len(num1)):
            for j in range(len(num2)):
                res[i+j]+=(int(num1_[i])*int(num2_[j]))
        carry=0
        
        for i in range(len(res)):
            
            tmp=res[i]+carry
            carry=(tmp)//10
            res[i]=str((tmp)%10)
            
        if carry>0:
            res.append(str(carry))
        idx=0
        for j in range(len(res)-1,-1,-1):
            if res[j]!='0':
                idx=j
                break
                
        return ''.join(res[:j+1][::-1])
