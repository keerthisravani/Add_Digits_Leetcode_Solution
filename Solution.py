class Solution:
    def addDigits(num):
        result=0
        if num<=9:
            return num
        while num>0:
            rem=num%10
            result=result+rem
            num=num//10
            if num==0:
                if result<=9:
                   return result
                num=result
                result=0
n=5
obj=Solution()
print(obj.addDigits(n))