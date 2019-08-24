#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr_p=0
        while curr_p<len(nums)-1:
            if nums[curr_p]==nums[curr_p+1]:
                del nums[curr_p]
                curr_p-=1
            curr_p+=1
        return len(nums)
