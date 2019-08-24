#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map={}
        for i,value in enumerate(nums):
            if target-value in hash_map:
                return [i,hash_map[target-value]]
            hash_map[value]=i
# 解题思路：
# 这里采用一遍hash的方式：新建一个空的字典，然后遍历数组，如果target-x在字典里面，则返回x和target-x的索引值，
# 如果不在则将该数值加入字典中。             


        

