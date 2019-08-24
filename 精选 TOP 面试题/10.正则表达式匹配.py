#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        import re
        return re.match('^'+p+'$',s)!=None

