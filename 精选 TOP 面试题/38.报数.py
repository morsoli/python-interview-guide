#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 报数
#
class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1: 
            return '1'
        res='1'
        while n>1:
            s,res,count=res,'',0
            for i in range(len(s)):
                count+=1
                if i==len(s)-1 or s[i]!=s[i+1]:
                    res+=str(count)
                    res+=s[i]
                    count=0
            n-=1
        return res
