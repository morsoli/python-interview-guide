#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#
class Solution:
    def romanToInt(self, s: str) -> int:
        result=0
        chars={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for i in range(len(s)-1):
            # 在左边的情况
            if chars[s[i]]<chars[s[i+1]]:
                result-=chars[s[i]]
            # 通常情况下，罗马数字中小的数字在大的数字的右边
            else:
                result+=chars[s[i]]
        result+=chars[s[-1]] 
        return result   
