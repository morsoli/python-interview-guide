#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        self.dfs(res,n,n,'')
        return res
    def dfs(self,res,left,right,path):
        if left==0 and right==0:
            res.append(path)
            return
        if left>0:
            self.dfs(res,left-1,right,path+'(')
        if left<right:
            self.dfs(res,left,right-1,path+')')
# 解题思路：最多能添加n个左括号，在递归调用的时候，在能传递到最底层的共用字符串中先添加”(“，然后left-1，递归调用就可以。
# 向下搜索要满足两个条件：插入数量不超过n，
# 可以插入 ） 的前提是 ( 的数量大于 ）
