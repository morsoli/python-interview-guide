#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while nums[i]>0 and nums[i]<=len(nums) and nums[nums[i]-1]!=nums[i]:
                nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1]
        for i in range(0,len(nums)):
            if nums[i]!=(i+1):
                return i+1
        return len(nums)+1
# 解题思路：将每个数放在它正确的位置，前提是该数是正数，并且该数小于序列长度，并且它正确位置上的那个数不是它，
# 也就是说，把4要放在第4个位置，要保证第4个位置上的数不是4，如果是4的话，交换前后没什么变换，把两个4移来移去，还会造成死循环。
# 从前往后看，发现在第n个位置本该出现的n没有出现，所有该序列缺失的第一个正数是n。
