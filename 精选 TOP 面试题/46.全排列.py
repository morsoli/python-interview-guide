#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = [0] * len(nums)
        res = []       
        def dfs(path):
            if len(path) == len(nums):
                res.append(path)
            else:
                for i in range(len(nums)):
                    if not visited[i]:
                        visited[i] = 1
                        dfs(path + [nums[i]])
                        visited[i] = 0
        
        dfs([])
        return res

