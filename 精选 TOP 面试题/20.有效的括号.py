#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2==1:
            return False
        map_dict={'{':'}','[':']','(':')'}
        stack=[]
        for i in s:
            # 左半边字符全入栈
            if i in map_dict:
                stack.append(i)
            else:
                # 第一个字符为右边符号或者一出现不匹配就直接返回false
                if not stack or map_dict[stack.pop()]!=i:
                    return False
        return stack==[]
