#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                return mid
            # 如果A[m]<A[r]，那么说明从m到r一定是有序的（没有受到rotate的影响）
            if nums[mid] < nums[right]:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target < nums[mid] and target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1 
# 解题思路：二分查找，重要的不是通过mid与左右指针指向的值的比较来移动指针，
# 而是通过判断那一部分是有序的，target是否在这个有序的切片之中来实现的。
