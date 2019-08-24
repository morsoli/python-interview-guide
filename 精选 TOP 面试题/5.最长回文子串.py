#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
class Solution:
    def longestPalindrome(self, s: str) -> str:
        start=0
        maxstr=0
        for i in range(len(s)):
            # 头和尾相同时，最长回文子串是去头去尾之后的部分的最长回文子串加上头和尾
            if i-maxstr>=1 and s[i-maxstr-1:i+1]==s[i-maxstr-1:i+1][::-1]:
                start=i-maxstr-1
                maxstr+=2
                continue
            # 头和尾不同，最长回文子串是去头的部分的最长回文子串和去尾的部分的最长回文子串中的较长的那一个。
            if s[i-maxstr:i+1]==s[i-maxstr:i+1][::-1]:
                start=i-maxstr
                maxstr+=1
        return s[start:start+maxstr]
       