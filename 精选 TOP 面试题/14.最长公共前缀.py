#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result=''
        zip_obj=zip(*strs)
        for obj in zip_obj:
            if(len(set(obj)))==1:
                result+=obj[0]
            else:
                break
        return result
