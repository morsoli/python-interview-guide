#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#
class Solution:
    def myAtoi(self, str: str) -> int:
        # 去除前面的空格
        str=str.strip()
        if len(str)==0:
            return 0
        # flag 正负标志, number 为返回整数
        number,flag=0,1
        if str[0]=='-':
            str=str[1:]
            flag=-1
        elif str[0]=='+':
            str=str[1:]
        for c in str:
            if c>='0' and c<='9':
                number=10*number+ord(c)-ord('0')
            else:
                break
        number=number*flag
        if number>2**31-1:
            return 2**31-1
        if number<-2**31:
            return -2**31
        return number
