#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#
class Solution:
    def reverse(self, x: int) -> int:
        if x>0:
            temp=int(str(x)[::-1])
        else:
            temp=-int(str(-x)[::-1])
        if temp<2**31-1 and temp>-2**31:
            return temp
        else:
            return 0
