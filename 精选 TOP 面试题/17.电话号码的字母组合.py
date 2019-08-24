#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=='':
            return []
        kvmaps = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        result = ['']
        for i in range(len(digits)):
            # 使用结果数组表示遍历到当前的位置已有的结果，那么再遍历下一个位置的时候，
            # 把这个位置能形成的所有结果和原来的进行两两组合。
            result=[c+w for w in kvmaps[digits[i]] for c in result]
        return result
