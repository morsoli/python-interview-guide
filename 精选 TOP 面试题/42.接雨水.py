#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left,right=0,len(height)-1
        # 用 left_max， right_max 记录走过的最高的边
        left_max=right_max=result=0
        while left<right:
            if height[left]<height[right]:
                if height[left]>left_max:
                    left_max=height[left]
                else:
                    result+=(left_max-height[left])
                # 继续移动左指针
                left+=1
            else:
                if height[right]>right_max:
                    right_max=height[right]
                else:
                    result+=(right_max-height[right])
                right-=1
        return result
# 解题思路：https://blog.csdn.net/XX_123_1_RJ/article/details/81048041
