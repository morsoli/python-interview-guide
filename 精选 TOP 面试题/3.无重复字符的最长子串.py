#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_str=0
        for i in range(len(s)):
            if len(s[i-max_str:i+1])==len(set(s[i-max_str:i+1])):
                max_str+=1
        return max_str
# 解题思路：滑动窗口法


